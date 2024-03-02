# exercise 6-4 glossary part 2
# add 5 more definitions and use a loop to print
glossary = {
    'dictionary': 'an object that consists of key, value pairs',
    'variable': 'a symbol used to store some data',
    'set': 'an iterable collection of items without duplicates',
    'print': 'a function for outputting data in a standard way',
    'key': 'an object used to access some value in a dictionary',
    'value': 'the value retrieved by a key from a dictionary',
    'function': 'a repeatable block of code',
    'list': 'an iterable collection of items similar to an array'
}

for key in glossary:
    print(f'{key.title()}:')
    print(f'     {glossary[key]}')
    if (key != 'list'):
        print()
