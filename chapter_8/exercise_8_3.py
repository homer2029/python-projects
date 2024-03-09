# exercise 8-3 t-shirt factory
# function that accepts size and message and prints a summary
# call with positional args
# call with keyword args
def make_shirt(size: str, message: str) -> None:
    """Prints a summary message about the t-shirt described by the size and message arguments.

    Args:
        size (str): t-shirt size (S, M, L, XL ... etc)
        message (str): a message to be printed on the shirt
    """
    print(
        f'Confirmed 1 T-Shirt Size: {size.upper()}\nMessage Reads: {message.title()}\n')


make_shirt('s', 'have a nice day')
make_shirt(message='eat my shorts', size='xl')
