from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from slowapi import errors, extension, middleware, util
from starlette.responses import RedirectResponse

from .exceptions import LyricsNotFound
from .utils import song

app = FastAPI()

limiter = extension.Limiter(
    key_func=util.get_remote_address, default_limits=["15/minute"]
)

app.state.limiter = limiter

app.add_exception_handler(
    errors.RateLimitExceeded, extension._rate_limit_exceeded_handler
)


app.add_middleware(middleware.SlowAPIMiddleware)


@app.get("/")
def index():
    return RedirectResponse(url="https://github.com/UltiRequiem/azlyrics_api")


@app.get("/{artist}/{title}")
@cache(expire=60)
async def author_song(artist: str, title: str):
    try:
        return song(title, artist)
    except LyricsNotFound:
        return {"error": f"Lyrics not found for {title} of artist {artist}."}
    except:
        return {"error": "Something went wrong."}


@app.get("/{title}")
@cache(expire=60)
async def song_endpoint(title: str):
    try:
        return song(title)
    except LyricsNotFound:
        return {"error": f"Lyrics not found for {title}."}
    except:
        return {"error": "Something went wrong."}


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())
