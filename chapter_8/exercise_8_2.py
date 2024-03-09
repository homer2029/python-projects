# exercise 8-2 favorite book
# function that accepts the argument title
# and outputs a message
def favorite_book(title: str) -> None:
    """Prints a message about a favorite book based on it's title.

    Args:
        title (str): The title of the book.
    """
    print(f'My favorite book is: {title.title()}.')


favorite_book("the hitchhiker's guide to the galaxy")
