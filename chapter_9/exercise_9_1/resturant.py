class Resturant:
    """ Resturant class describes a resturant.
    """

    def __init__(self, name: str, cusine_type: str):
        """ Creates a new resturant.

        Args:
            name (str): Name of the resturant.
            cusine_type (str): Type of food resturant makes.
        """
        self.name = name
        self.cusine_type = cusine_type

    def describe_resturant(self) -> None:
        """ Prints a description of a resturant.
        """
        print(f'name: {self.name}\ncusine_type: {self.cusine_type}')

    def open_resturant(self) -> None:
        """ Prints a message indicating the resturant is open.
        """
        print(f'{self.name.title()} is now open.')
