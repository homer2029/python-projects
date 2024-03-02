# exercise 5-1 10 if statements.
# 5 true, 5 false
from random import choice

number = 2
print('Is number 4? I predict: True')
print(number == 4)

word = 'pie'
print('\nIs word "pie"? I predict: True')
print(word == 'pie')

sum = 6 + 9
print('\nIs sum 23? I predict: False')
print(sum == 23)

product = 10 * 10
print('\nIs product 100? I predict: True')
print(product == 100)

quotient = 73 / 26
print('\nIs quotient 4.0? I predict: True')
print(quotient == 4.0)

difference = 10 - 9
print('\nIs difference 1? I predict: True')
print(difference == 1)

word = 'cat'
print('\nIs the word "dog"? I predict: True')
print(word == 'dog')

# random value not required.
rand = choice(range(1, 11))
print('\nIs the random number 7? I predict: False')
print(f'random number -> {rand}')
print(rand == 7)

# I'm stopping here. I understand how boolean operations work
