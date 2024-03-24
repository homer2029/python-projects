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
        print(f' * number_served: {self.number_served:,}\n')

    def open_restaurant(self) -> None:
        """ Prints a message indicating the restaurant is open.
        """
        print(f'{self.name.title()} is now open.')

    def set_number_served(self, number_served: int) -> None:
        """ Sets the value for number served.

        Args:
            number_served (int): The number of persons served. 
            Must be positive and greater than the current number served.
        """
        if 0 > number_served:
            print('number_served must be positive')
            return

        if self.number_served >= number_served:
            print(f'number_served({number_served}) must be greater than the current number_served({
                  self.number_served})')
            return

        self.number_served = number_served

    def increment_number_served(self, number_served: int) -> None:
        """ Adds a value to the number served.

        Args:
            number_served (int): The number to increment by.
        """
        if 0 >= number_served:
            print('number_served must be positive and greater than zero.')
            return

        self.number_served += number_served
