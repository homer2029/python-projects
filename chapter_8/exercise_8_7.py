# exercise 8-7 album
# function make album builds/returns dictionary
# params artist, album, none number of songs
# use at least 3 times, at least once with num songs
def make_album(artist: str, album_name: str, number_of_songs=None) -> dict[str, str]:
    """Creates a new dictionary that represents an album with artist, album_name, and optional
    number_of_songs keys.

    Args:
        artist (str): The artist that created the album.
        album_name (str): The name of the album.
        number_of_songs (int, optional): The number of songs on the album. Defaults to None.

    Returns:
        dict[str, str]: The new album dictionary.
    """
    album = {
        'artist': artist.title(),
        'album_name': album_name.title()
    }
    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album


album1 = make_album('operation ivy', 'energy', 19)
album2 = make_album('bad religion', 'suffer')
album3 = make_album('rancid', '...and out come the wolves', 19)

albums = [album1, album2, album3]
for album in albums:
    for key, value in album.items():
        print(f'{key} -> {value}')
    print()
