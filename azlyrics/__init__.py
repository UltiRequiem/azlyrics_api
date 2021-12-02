from fastapi import FastAPI
from slowapi import errors, extension, middleware, util

from .utils import get_song_data

app = FastAPI()

limiter = extension.Limiter(
    key_func=util.get_remote_address, default_limits=["15/minute"]
)

app.state.limiter = limiter

app.add_exception_handler(
    errors.RateLimitExceeded, extension._rate_limit_exceeded_handler
)


app.add_middleware(middleware.SlowAPIMiddleware)

# TODO: Cache response


@app.get("/{artist}/{title}")
async def author_song(artist: str, title: str):
    return get_song_data(title, artist)


@app.get("/{title}")
async def song(title: str):
    return get_song_data(title)
