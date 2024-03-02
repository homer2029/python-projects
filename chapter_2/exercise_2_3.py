# exercise 2-3 string formatting
person = 'Jackson'
message = f'Hello {person}.'

print(message)

person = 'Aaron'
message = f'Happy Birthday {person}!'

print(message)

# val = 12345
# val_2 = 123.456
# val_3 = 'Some other value.'
# single line multi-variable instantiation
val, val_2, val_3 = 12345, 123.456, 'Some other value.'
message = f'Did you know that you can put anything in these strings! {val}, {val_2}, {val_3}'

print(message)