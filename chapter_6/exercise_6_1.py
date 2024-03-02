# exercise 6-1 person dictionary
# person with first and last name and city of residence in a dictionary
# print all the keys/values
person_1 = {
    'first name': 'Aaron',
    'last name': 'Mills',
    'city of residence': 'Springfield',
    'state of residence': 'Missouri'
}

for key, val in person_1.items():
    # prints a left justified key with 19 spaces of padding
    print(f'person_1[ {key: <19}] -> {val}')
