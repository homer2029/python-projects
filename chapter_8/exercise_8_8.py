# exercise 8-8 user albums
# recreate exercise 8-7 but this time with user input and flow controll in a while loop
# i went a little bit off the reservation with my implementation here... :-)  XD
import sys


artist_prompt = 'Input an artist: '
album_prompt = 'Input an album name: '
songs_prompt = 'Input a number of songs on the album (optional): '
add_another = 'Add another album (y)es/(n)o: '


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


def stop_running(val: str) -> bool:
    """Determines if the program should contiue running.

    Args:
        val (str): The user's input.

    Returns:
        bool: Whether or not to keep running.
    """
    while val.lower() not in ['n', 'no', 'y', 'yes']:
        val = input(add_another)

    return val.lower() in ['n', 'no']


def main_pgm_loop() -> None:
    """The main loop of the program.
    """
    while True:
        artist_in = input(artist_prompt)
        album_in = input(album_prompt)
        songs_in = input(songs_prompt)

        album = make_album(artist=artist_in, album_name=album_in,
                           number_of_songs=songs_in)
        for key, value in album.items():
            print(f'album[{key}]: {value}')
        print()

        another_in = input(add_another)
        if stop_running(another_in):
            print('Good bye!')
            break


def main(*args, **kwargs) -> None:
    """Kinda like Java's public static void main... not really tho.
    """
    print('Album Generator \n')
    main_pgm_loop()


if __name__ == '__main__':
    main(sys.argv)
