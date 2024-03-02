# exercise 6-7 people
# at lease three people in a list.
# loop print values
person_1 = {
    'first name': 'Aaron',
    'last name': 'Mills',
    'city of residence': 'Springfield',
    'state of residence': 'Missouri'
}

person_2 = {
    'first name': 'Jackson',
    'last name': 'Mills',
    'city of residence': 'Springfield',
    'state of residence': 'Missouri'
}

person_3 = {
    'first name': 'Amelia',
    'last name': 'Mills',
    'city of residence': 'Springfield',
    'state of residence': 'Missouri'
}

person_4 = {
    'first name': 'Sarah',
    'last name': 'Buhr',
    'city of residence': 'Springfield',
    'state of residence': 'Missouri'
}

people = [person_1, person_2, person_3, person_4]

for person in people:
    full_name = f'{person["first name"]} {person["last name"]}'
    location = f'{person["city of residence"]}, {person["state of residence"]}'
    print(f'person:     {full_name}')
    print(f'resides in: {location}')
    print()
