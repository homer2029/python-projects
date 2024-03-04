# exercise 7-5 movie tickets
# ask for user's age
# different price based on an age
# below 3 -> $0
# 3 - 12 -> $10
# above 12 -> $15
# exit on q/quit
prompt = 'Input your age to determine ticket price: '
ticket_info = 'Your ticket price is: ${:0.2f}.'

while True:
    age = input(prompt)
    try:
        age = int(age)
        if (3 > age):
            print(ticket_info.format(0))
        elif (3 <= age and 12 >= age):
            print(ticket_info.format(10))
        else:
            print(ticket_info.format(15))
    except ValueError:
        if ('q' == str(age).lower() or 'quit' == str(age).lower()):
            print('Good bye!')
            break
        else:
            print('Please input a number.')
