# exercise 6-10 aka 6-2 enhanced
# add a list of numbers to peoples favorite number
# print name and list
favorite_numbers = {}
favorite_numbers['Jackson'] = [14, 7, 93]
favorite_numbers['Amelia'] = [7, 42, 14, 68, 63]
favorite_numbers['Sarah'] = [22, 18]
favorite_numbers['Aaron'] = [91, 99_000, 1981, 2004]
favorite_numbers['Nate'] = [27.563]

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print()
