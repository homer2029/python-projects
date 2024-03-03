# exercise 7-3 multiples of ten
# seek number input
# output if it is a multiple of 10
val = input('Input a number: ')

# this is more than was required of this assignment, but I didn't want to just accept anything...
while isinstance(val, str):
    try:
        val = int(val)
    except ValueError:
        val = input('\nInput MUST be a number: ')

if (0 == val % 10):
    print(f'\n{val} is a multiple of 10.')
else:
    print(f'\n{val} is not a multiple of 10.')
