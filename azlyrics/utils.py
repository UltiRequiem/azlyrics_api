from azapi import AZlyrics

from .exceptions import LyricsNotFound


def song(title: str, artist: str = ""):
    AZL = AZlyrics(search_engine="google", accuracy=0.3)

    AZL.artist, AZL.title = artist, title

    AZL.getLyrics()

    if AZL.lyrics == "":
        raise LyricsNotFound()

    result = vars(AZL)

    for key in ["songs", "lyrics_history", "proxies", "accuracy", "search_engine"]:
        result.pop(key)

    return result
