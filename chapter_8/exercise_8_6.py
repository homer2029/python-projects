# exercise 8-6 cities formatter
# function city country returns a formatted string
# call at least 3 times and print the output
def city_country(city: str, country: str) -> str:
    """Creates formatted city, country string.

    Args:
        city (str): The city in question.
        country (str): The country in question.

    Returns:
        str: The formatted string in the form city, country (title case).
    """
    return f'{city.title()}, {country.title()}'


cc1 = city_country('santiago', 'chile')
cc2 = city_country('rio de janeiro', 'brazil')
cc3 = city_country('buenos aires', 'argentina')

print(cc1)
print(cc2)
print(cc3)
