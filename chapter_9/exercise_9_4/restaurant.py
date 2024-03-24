class Restaurant:
    """ Restaurant class describes a resturant.
    """

    def __init__(self, name: str, cusine_type: str):
        """ Creates a new restaurant.

        Args:
            name (str): Name of the restaurant.
            cusine_type (str): Type of food restaurant makes.
        """
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self) -> None:
        """ Prints a description of a restaurant.
        """
        print(f' * name: {self.name.title()}')
        print(f' * cusine_type: {self.cusine_type.title()}')
        print(f' * number_served: {self.number_served}\n')

    def open_restaurant(self) -> None:
        """ Prints a message indicating the restaurant is open.
        """
        print(f'{self.name.title()} is now open.')
