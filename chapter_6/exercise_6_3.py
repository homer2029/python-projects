# exercise 6-3 glossary
# pick three words and store their definitions in a dictionary
# print the formatted glossary
# I guess this wasn't supposed to be a loop...
glossary = {
    'dictionary': 'an object that consists of key, value pairs',
    'variable': 'a symbol used to store some data',
    'list': 'an iterable collection of items similar to an array'
}

# for key in glossary:
#     print(f'{key.title()}:')
#     print(f'     {glossary[key]}')
#     print()

print(f'{'dictionary'.title()}:')
print(f'     {glossary.get('dictionary', 'no definition')}')
print()

print(f'{'variable'.title()}:')
print(f'     {glossary.get('variable', 'no definition')}')
print()

print(f'{'list'.title()}:')
print(f'     {glossary.get('list', 'no definition')}')
