# exercise 6-5 rivers create a dictionary of rivers and countries
# print a sentence that contains both the river and the country
# print a sentence for just the river
# print a sentence for just the country
# loops!!!
def add_the(country: str):
    if ('united states' == country):
        return 'the ' + country
    return country


rivers = {
    'thames': 'england',
    'missouri': 'united states',
    'rhine': 'germany'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {add_the(country).title()}.')

print()

for river in rivers.keys():
    print(f'The {river.title()} is indeed a river.')

print()

for country in rivers.values():
    print(f'{add_the(country).title()} is indeed a country.')
