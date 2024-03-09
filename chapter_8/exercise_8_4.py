# exercise 8-4 large t-shirts
# recreate exercise 8-3 but include defalut values in function signature
# default size = large; default message = i love python
# call multiple ways
def make_shirt(size: str = 'l', message: str = 'i love python') -> None:
    """Prints a summary message about the t-shirt described by the size and message arguments.

    Args:
        size (str, optional): t-shirt size (S, M, L, XL ... etc). Defaults to 'L'.
        message (str, optional): a message to be printed on the shirt. Defaults to 'i love python'.
    """
    print(
        f'Confirmed 1 T-Shirt Size: {size.upper()}\nMessage Reads: {message.title()}\n')


make_shirt()
make_shirt('m')
make_shirt('s', 'horse thieves')
