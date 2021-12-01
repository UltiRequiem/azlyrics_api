from fastapi import FastAPI
from slowapi import errors, extension, util
from .utils import get_song

app = FastAPI()
limiter = extension.Limiter(key_func=util.get_remote_address)

app.state.limiter = limiter

app.add_exception_handler(
    errors.RateLimitExceeded, extension._rate_limit_exceeded_handler
)


@app.get("/{author}/{song}")
async def author_song(author: str, song: str):
    return get_song(song, author)


@app.get("/{song}")
async def song(song: str):
    return get_song(song)
