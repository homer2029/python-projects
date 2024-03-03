# exercise 7-4 pizza toppings
# accept pizza toppings as input
# continue untill the user quits
# function not required
def exit_loop(topping: str) -> bool:
    return 'q' == topping.lower() or 'quit' == topping.lower()


topping = input('Add a topping to your pizza: ')
toppings = []

while not exit_loop(topping):
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
