# ordinal numbers
# list 1-9
# print each ordinal 1st, 2nd, 3rd...9th on a seperate line
# for loop with if elif else
numbers = [num for num in range(1, 10)]

# if only implementation
# for number in numbers:
#     if (1 == number):
#         print(f'{number}st')
#     if (2 == number):
#         print(f'{number}nd')
#     if (3 == number):
#         print(f'{number}rd')
#     if (4 <= number):
#         print(f'{number}th')

# if-elif implementation
# for number in numbers:
#     if (1 == number):
#         print(f'{number}st')
#     elif (2 == number):
#         print(f'{number}nd')
#     elif (3 == number):
#         print(f'{number}rd')
#     elif (4 <= number):
#         print(f'{number}th')

# if-elif-else implementation; what the exercise called for
# for number in numbers:
#     if (1 == number):
#         print(f'{number}st')
#     elif (2 == number):
#         print(f'{number}nd')
#     elif (3 == number):
#         print(f'{number}rd')
#     else:
#         print(f'{number}th')

# match-case statement implementation
# aparently there's no fall through in python match-case
for number in numbers:
    match number:
        case 1:
            print(f'{number}st')
        case 2:
            print(f'{number}nd')
        case 3:
            print(f'{number}rd')
        case _:  # default case
            print(f'{number}th')
