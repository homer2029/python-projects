# exercise 4-2 animals
# list at least 3 animals with a common characteristic
# for loop print each animal
# for loop f-string each animal
# summary line at the end
animals = ['zebra', 'lion', 'elephant']
for animal in sorted(animals):
    print(animal)  # elephant, lion, zebra

print()

for animal in animals:
    print(f'{animal.title()}s belong in the wild and NOT in a zoo.')

print("\nThat's how I feel about those animals.")
