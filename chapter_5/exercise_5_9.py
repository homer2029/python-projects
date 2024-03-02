# exercise 5-9 hello admin with empty list check.
# bits copied from 5-8
def print_users_list(users: list):
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, enjoy your total controll of everything.')
        else:
            print(f'Hello {user}, welcome back.')


users = []

if users:
    print_users_list(users)
else:
    print('Users list is empty; get some users.')

print('Getting users...')
users = ['Jackson', 'Aaron', 'admin', 'Amelia', 'Sarah', 'Shawn']

if users:
    print_users_list(users)
else:
    print('Users list is empty; get some users.')
