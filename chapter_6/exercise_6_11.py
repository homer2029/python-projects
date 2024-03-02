# exercise 6-11 cities
# at least 3 cities as keys in dict
# value is info about the city -> country, pop, fact
# print outputs
import locale
locale.setlocale(locale.LC_ALL, '')


# def make_title(datum):
#     if isinstance(datum, str):
#         return datum.title()
#     return f'{datum:n}'


cities = {
    'london': {
        'country': 'england',
        'population': 8_799_800,
        'fact': 'capital of england and the united uingdom.'
    },
    'paia': {
        'country': 'united states',
        'population': 2_470,
        'fact': 'on the island of maui, beautiful senic views.'
    },
    'lisbon': {
        'country': 'portagual',
        'population': 548_703,
        'fact': 'lisbon is one of the oldest cities in the world.'
    }
}

for city, infos in cities.items():
    print(f'{city.title()}:')
    for info, datum in infos.items():
        # print(f'  * {info.title()} -> {make_title(datum)}')
        # swapped to python's wonky terinary operator
        print(f'  * {info.title()} -> {datum.title()
              if isinstance(datum, str) else f"{datum:n}"}')
    print()
