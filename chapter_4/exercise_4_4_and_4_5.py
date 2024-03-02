# exercise 4-4 list 1 to 1,000,000 and print
one_to_one_million = [value for value in range(1, 1_000_001)]
for i in one_to_one_million:
    if i % 50_000 == 0:  # it takes a LONG time to count to 1,000,000 in Python; let's only print every 50,000
        print(i)

print(f'\nMax value in list -> {max(one_to_one_million)
                                }\nMin value in list -> {min(one_to_one_million)}')
print()

# exercise 4-5 min max and sum on one to one million
print(f'min: {min(one_to_one_million)}')
print(f'max: {max(one_to_one_million)}')
print(f'sum: {sum(one_to_one_million)}')
