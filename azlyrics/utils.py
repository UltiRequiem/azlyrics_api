import azapi


async def get_song(artist: str, title: str):
    azl = azapi.AZlyrics("google", accuracy=0.5)

    azl.artist = artist
    azl.title = title

    azl.getLyrics(sleep=0)

    return azl
