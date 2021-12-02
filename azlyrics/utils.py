import azapi


class NoLyricsFound(BaseException):
    pass


def get_song(title: str, artist: str = ""):
    azl = azapi.AZlyrics("google", accuracy=0.5)

    azl.artist, azl.title = artist, title

    azl.getLyrics()

    if azl.lyrics == "":
        raise NoLyricsFound(f"No lyrics found for {title}.")

    for key in ["songs", "lyrics_history", "proxies", "accuracy", "search_engine"]:
        azl.__dict__.pop(key)

    return azl.__dict__


def get_song_data(title: str, artist: str = ""):
    try:
        return get_song(title, artist)
    except NoLyricsFound as e:
        return {"error": str(e)}
