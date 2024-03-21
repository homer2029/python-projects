class User:
    """ A user with personal info.
    """

    def __init__(self, first_name: str, last_name: str,
                 age: int | None = None, email: str | None = None, **extra_info):
        """ Creates a new user

        Args:
            first_name (str): user's first name
            last_name (str): user's last name
            age (int | None, optional): user's age. Defaults to None.
            email (str | None, optional): user's email address. Defaults to None.
            extra_info (kwargs): any extra info about the user. Kwargs.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.extra_info = extra_info

    def describe_user(self) -> None:
        """ Prints a description of a user and all available properties.
        """
        print(f'first_name -> {self.first_name.capitalize()}')
        print(f'last_name -> {self.last_name.capitalize()}')
        if (self.age):
            print(f'age -> {self.age}')
        if (self.email):
            print(f'email -> {self.email}')
        if (self.extra_info):
            for key, val in self.extra_info.items():
                print(f'{key} -> {val}')

    def greet(self) -> None:
        """ Prints a greeting to the user.
        """
        print(f'Hello {self.first_name.capitalize()} {
              self.last_name.capitalize()}.')
