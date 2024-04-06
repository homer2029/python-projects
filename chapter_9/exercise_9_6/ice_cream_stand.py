from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """ A specific type of restaurant that only serves ice cream.

    Args:
        Restaurant (_type_): a restaurant.
    """

    def __init__(self, name: str, flavors: list[str], cusine_type='ice cream'):
        """ Creates a new ice cream stand.

        Args:
            name (str): Name of the restaurant.
            cusine_type (str): Type of food restaurant makes.
            flavors (list[str]): The flavors of ice cream served.
        """
        super().__init__(name, cusine_type)
        self.flavors = flavors

    def display_flavors(self) -> None:
        """ Displays all available ice cream flavors.
        """
        print(f'{self.name.capitalize()} serves the following ice cream flavors:')
        for flavor in self.flavors:
            print(flavor.title())
