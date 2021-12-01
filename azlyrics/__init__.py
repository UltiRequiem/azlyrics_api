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
async def root(author: str, song: str):
    song_data = get_song(author, song)

    return (
        {"error": f"No lyrics found for {song}, {author}"}
        if song_data.lyrics == ""
        else {
            "lyrics": song_data.lyrics,
            "author": song_data.artist,
            "title": song_data.title,
        }
    )
