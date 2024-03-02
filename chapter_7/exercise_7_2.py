# exercise 7-2 resturant seating
# ask for number of dinners
# if 8 or more respond "you'll have to wait"
# else "we'll seat you now"
prompt = 'How many will be dining with you tonight? '
val = input(prompt)
num_diners = int(val)
if (8 >= num_diners):
    print('We will happily seat you now.')
else:
    print("You'll have to wait to be seated.")
