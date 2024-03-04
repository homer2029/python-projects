# exercise 7-6 3 exits
# rewrite exercise 7-4 or 7-5 with 3 different loop exits
# 1 ) active variable
# 2 ) break
# 3 ) conditional
# i'm gonna split this up into 3 different files and use 7-4 for my template program
# this will be exercise 7-6a active variable
topping = input('Add a topping to your pizza: ')
toppings = []
active = True

while active:
    if 'q' == topping.lower() or 'quit' == topping.lower():
        active = False
    else:
        print(f'Adding {topping} to your pizza.')
        toppings.append(topping)
        topping = input('Add another topping to your pizza? or (q)uit? ')

# loop print of toppings not required
if toppings:
    print('\nYour pizza has the following toppings:')
    for t in toppings:
        print(f'    {t}')
else:
    print("\nYou've got no toppings; cheese pizza only.")
