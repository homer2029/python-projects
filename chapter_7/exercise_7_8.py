# exercise 7-8 deli
# two lists 'sandwich_orders' and 'finished_sandwiches'
# loop through 'so' and print + add to 'fs'
# print a final list of 'fs'
sandwich_orders = ['peanut butter + jelly', 'pastrami on rye',
                   'club', 'tuna melt', 'cuban', 'roast beef w/provolone']
finished_sandwiches = []

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
