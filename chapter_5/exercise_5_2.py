# exercise 5-2 more conditionals
# equality and inequality in strings
# string with lower
# numeric tests ==; !=; <; >; <=; >=
# test with or
# an item is in a list
# an item is not in a list
word = 'ewww'
word_2 = 'gross'
word_3 = 'EWWW'

print(f'{word} == {word} -> {word == word}')
print(f'{word} != {word_2} -> {word != word_2}')
print(f'{word} != {word_3} -> {word != word_3}')
print(f'{word} == {word_3}.lower() -> {word == word_3.lower()}')

num = 24
num_2 = 32
num_3 = 6 * 4

print(f'\n{num} == {num_3} -> {num == num_3}')
print(f'{num} != {num_2} -> {num != num_2}')
print(f'{num_2} > {num} -> {num_2 > num}')
print(f'{num} < {num_2} -> {num < num_2}')
print(f'{num} <= {num_3} -> {num <= num_3}')
print(f'{num_2} >= {num_3} -> {num_2 >= num_3}')

this = 'abc'
that = 'ABC'
the_other = 'aBc'

if this == that.lower() or that != the_other:
    print('\nthis equal that or not equal the other!')
else:
    print('\nwrong, you loose')

some_list = [16, 53, 2.7, 99, 106]
if 16 in some_list:
    print('\ncool story bro...')
else:
    print('\naww... too bad... no good numbers in that list.')

if 32 not in some_list:
    print('\naww... too bad... no good numbers in that list.')
