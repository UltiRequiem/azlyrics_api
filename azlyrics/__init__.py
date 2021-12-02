from fastapi import FastAPI
from slowapi import errors, extension, util, middleware
from .utils import get_song

app = FastAPI()

limiter = extension.Limiter(
    key_func=util.get_remote_address, default_limits=["15/minute"]
)

app.state.limiter = limiter

app.add_exception_handler(
    errors.RateLimitExceeded, extension._rate_limit_exceeded_handler
)


app.add_middleware(middleware.SlowAPIMiddleware)


@app.get("/{artist}/{title}")
async def author_song(artist: str, title: str):
    return get_song(title, artist)


@app.get("/{title}")
async def song(title: str):
    return get_song(title)
