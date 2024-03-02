# exercise 6-8 pets
# details about a pet
# pets in list
# loop and print
from operator import itemgetter


pet_1 = {}
pet_1['type'] = 'dog'
pet_1['age'] = 5
pet_1['color'] = 'golden brown'
pet_1['name'] = 'luna'
pet_1['owner'] = 'the mills family'

pet_2 = {}
pet_2['type'] = 'cat'
pet_2['age'] = 2
pet_2['color'] = 'grey/white'
pet_2['name'] = 'darcy'
pet_2['owner'] = 'grape-a'

pet_3 = {}
pet_3['type'] = 'fish'
pet_3['age'] = 3
pet_3['color'] = 'silver'
pet_3['name'] = 'zinny'
pet_3['owner'] = 'amelia mills'

pet_4 = {}
pet_4['type'] = 'fish'
pet_4['age'] = 3
pet_4['color'] = 'silver'
pet_4['name'] = 'carin'
pet_4['owner'] = 'amelia mills'

pets = []
pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)
pets.append(pet_4)

# sorting my list by pet name
# for pet in sorted(pets, key=lambda p: p['name'], reverse=True):
#     print(f'Name: {pet['name'].title()}')
#     print(f'Age: {pet.get('age', 0)}')
#     print(f'Type: {pet.get('type')}')
#     print(f'Color: {pet['color']}')
#     print(f'Owner: {pet.get('owner').title()}')
#     print()

# does the same as above, with operator.itemgetter; works with dictionaries
# operator.attrgetter works with proper objects.
for pet in sorted(pets, key=itemgetter('name'), reverse=True):
    print(f'Name: {pet['name'].title()}')
    print(f'Age: {pet.get('age', 0)}')
    print(f'Type: {pet.get('type')}')
    print(f'Color: {pet['color']}')
    print(f'Owner: {pet.get('owner').title()}')
    print()
