# exercise 4-8 first 10 cubes eg 1^3 - 10^3
cubes = []
for val in range(1, 11):
    cubes.append(val**3)

for cube in cubes:
    print(cube)

print()

# exercise 4-9 list comprehension of 4-8
comprehension_cubes = [i**3 for i in range(1, 11)]
for comp_cube in comprehension_cubes:
    print(comp_cube)
