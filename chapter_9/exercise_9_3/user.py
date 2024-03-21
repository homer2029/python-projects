class User:
    """ A user with personal info.
    """

    def __init__(self, first_name: str, last_name: str, age: int | None = None, email: str | None = None):
        """ Creates a new user

        Args:
            first_name (str): user's first name
            last_name (str): user's last name
            age (Optional[int], optional): user's age. Defaults to None.
            email (Optional[str], optional): user's email address. Defaults to None.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self) -> None:
        """ Prints a description of a user and all available properties.
        """
        print(f'first_name -> {self.first_name.capitalize()}')
        print(f'last_name -> {self.last_name.capitalize()}')
        if (self.age):
            print(f'age -> {self.age}')
        if (self.email):
            print(f'email -> {self.email}')

    def greet(self) -> None:
        """ Prints a greeting to the user.
        """
        print(f'Hello {self.first_name.capitalize()} {
              self.last_name.capitalize()}.')
