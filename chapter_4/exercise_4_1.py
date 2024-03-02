# exercise 4-1 pizza
# list of 3 kinds of pizza
# for loop print pizza
# for loop print f-string about pizza
# summary print at the end
pizzas = ['pepperoni and bacon', 'mushroom and black olive',
          'chicken and kalamata olive']
for pizza in pizzas:
    print(pizza)

print()

for pizza in pizzas:
    print(f'I like to eat {pizza} pizza.')

print()

print(f'I like {len(pizzas)} different kinds of pizza.')
