# definitely NOT required here, just messing about
def __new_line__():
    print('')

# exercise 3-4 use a list and invite people to dinner.
dinner_guests = ['Sarah', 'Jackson', 'Amelia']
print(dinner_guests)
__new_line__()

# I don't think this is the expected implementation here, but, I wanted to get fancy
message = '{0}, I would like to invite you to dinner.'
print(message.format(dinner_guests[0]))
print(message.format(dinner_guests[1]))
print(message.format(dinner_guests[2]))
__new_line__()

# exercise 3-5 modify the dinner guests to remove one person and add another
# making a copy, so I have a pristine version of the list (not required)
dinner_guests_3_5 = dinner_guests.copy()

# definitely not the intended solution, but, it's what I wanted to do
can_t_make_it = dinner_guests_3_5.pop(dinner_guests_3_5.index('Jackson'))
print(f"Oh noes, {can_t_make_it} can't make it.")
__new_line__()
print(dinner_guests_3_5)
__new_line__()
print(message.format(dinner_guests_3_5[0]))
print(message.format(dinner_guests_3_5[1]))
__new_line__()

# exercise 3-6 adding people to the list
dinner_guests_3_6 = dinner_guests.copy()
print('Hey, guess what? I got a bigger table, more people can come!')
__new_line__()

print(dinner_guests_3_6)
dinner_guests_3_6.insert(0, 'Phyllis')
dinner_guests_3_6.append('Dave')
dinner_guests_3_6.insert(2, 'Pam')
print(dinner_guests_3_6)
__new_line__()
print(message.format(dinner_guests_3_6[0]))
print(message.format(dinner_guests_3_6[1]))
print(message.format(dinner_guests_3_6[2]))
print(message.format(dinner_guests_3_6[3]))
print(message.format(dinner_guests_3_6[4]))
print(message.format(dinner_guests_3_6[5]))
__new_line__()

# exercise 3-7 pop/remove guests from 3-6
dinner_guests_3_7 = dinner_guests_3_6.copy()
print(dinner_guests_3_7)

uninvited = '{0} uninvited...'
print(uninvited.format(dinner_guests_3_7.pop()))
print(dinner_guests_3_7)
print(uninvited.format(dinner_guests_3_7.pop()))
print(dinner_guests_3_7)
print(uninvited.format(dinner_guests_3_7.pop()))
print(dinner_guests_3_7)
print(uninvited.format(dinner_guests_3_7.pop()))
print(dinner_guests_3_7)
__new_line__()
print(message.format(dinner_guests_3_7[0]))
print(message.format(dinner_guests_3_7[1]))

__new_line__()
print("Get rid of 'em all.")
dinner_guests_3_7.remove(dinner_guests_3_7[0])
dinner_guests_3_7.remove(dinner_guests_3_7[0])
print(dinner_guests_3_7)