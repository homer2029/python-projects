# exercise 7-9 no pastrami
# recreate 7-8, but make sure there are 3+ 'pastrami' sandwiches in the 'sandwich_orders'
# output a message saying that we're out of pastrami
# remove all pastrami from the orders in while loop
# then complete 7-8 business as usual
sandwich_orders = ['pastrami', 'peanut butter + jelly', 'pastrami',
                   'club', 'pastrami', 'tuna melt', 'cuban', 'roast beef w/provolone', 'pastrami']
finished_sandwiches = []

print("We're all out of pastrami... ...no pastrami sandwiches today!")
num_pastrami_sandwiches = 0
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    num_pastrami_sandwiches += 1

print(
    f'Removed {num_pastrami_sandwiches} pastrami sandwiches from sandwich_orders.')
print()

while sandwich_orders:
    # pop(0) keeps the list in order; pop() reverses the list
    sandwich = sandwich_orders.pop(0)
    print(f'I just made a {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

# not required - just for fun...
if not sandwich_orders:
    print('\nHere are the sandwiches I made:')
    for sandwich in finished_sandwiches:
        print(f' * {sandwich}')
else:
    print('Looks like I forgot to make a sandwich.')
