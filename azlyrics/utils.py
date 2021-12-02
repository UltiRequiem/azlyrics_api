import functools

import azapi


@functools.cache
def get_song(title: str, artist: str = ""):
    azl = azapi.AZlyrics("google", accuracy=0.5)

    azl.artist = artist
    azl.title = title

    azl.getLyrics()

    if azl.lyrics == "":
        return {"error": f"No lyrics found for {title}."}

    data = azl.__dict__

    for key in ["songs", "lyrics_history", "proxies", "accuracy", "search_engine"]:
        data.pop(key)

    return data
