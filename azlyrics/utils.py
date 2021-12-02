import azapi

from .exceptions import LyricsNotFound


async def get_song(title: str, artist: str = ""):
    azl = azapi.AZlyrics("google", accuracy=0.5)

    azl.artist, azl.title = artist, title

    azl.getLyrics(sleep=0)

    if azl.lyrics == "":
        raise LyricsNotFound(f"No lyrics found for {title}.")

    for key in ["songs", "lyrics_history", "proxies", "accuracy", "search_engine"]:
        azl.__dict__.pop(key)

    return azl.__dict__
