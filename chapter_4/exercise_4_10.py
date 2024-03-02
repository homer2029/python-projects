# exercise 4-10 slices
# list of something decent number of things
# print slice of first 3 items
# print slice of middle 3 items
# print slice of last 3 items
squares = [i**2 for i in range(1, 14)]
print(squares)  # not required
first_three = squares[:3]
print(first_three)
mid_point = int(len(squares)/2) - 1
middle_three = squares[mid_point:(mid_point + 3)]
print(middle_three)
last_three = squares[-3:]
print(last_three)
