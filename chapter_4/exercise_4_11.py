# exercise 4-11 pizzas mine and a friends
# pizzas lifted from 4-1
pizzas = ['pepperoni and bacon', 'mushroom and black olive',
          'chicken and kalamata olive']
friend_s_pizzas = pizzas[:]
pizzas.append('sausage and ham')
friend_s_pizzas.append('hawaiian')

for pizza in pizzas:
    print(f'My {pizza} pizza.')

print()
for pizza in friend_s_pizzas:
    print(f'Your {pizza} pizza.')

print('\nDifferent pizzas in both lists.')

# below is not required just a simplistic difference implementation
unique_pizzas = []
for pizza in pizzas:
    if 0 == friend_s_pizzas.count(pizza):
        unique_pizzas.append(pizza)

for pizza in friend_s_pizzas:
    if 0 == pizzas.count(pizza):
        unique_pizzas.append(pizza)

print('\nUnique pizzas:')
for pizza in unique_pizzas:
    print(pizza)
