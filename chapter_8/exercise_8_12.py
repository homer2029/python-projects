# exercise 8-12 sandwiches
# the varargs problem
# function that accepts a variable list of arguments
# call it with at least 3 different sets of args
def make_sandwich(*toppings: str) -> None:
    """Method prints a sandwich with various toppings

        Args:
            *toppings (str): Arbitrary tuple of string values. args
    """
    size = len(toppings)
    print(
        f'\nNow making a sandwich with {size} {'topping' if 1 == size else 'toppings'}.')
    for topping in toppings:
        print(f'  * Added: {topping.upper()}')


make_sandwich('roast beef')
make_sandwich('turkey', 'ham', 'swiss cheese', 'mustard')
make_sandwich('tuna salad', 'pickles')
make_sandwich('peanut butter', 'bacon', 'jelly')
