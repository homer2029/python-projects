# exercise 8-5 cities
# function describe city
# two params city and country
# prints a simle sentence
# country has a default
# three calls at least one without the default country
def describe_city(city: str, country: str = 'usa') -> None:
    """Prints a message about a city.

    Args:
        city (str): The city in question.
        country (str, optional): The country in question. Defaults to 'usa'.
    """
    print(f'{city.title()} is a city in {country.title()
          if 'usa' != country.lower() else country.upper()}.')


describe_city('springfield')
describe_city('new york')
describe_city('london', 'england')
describe_city('paris', 'france')
