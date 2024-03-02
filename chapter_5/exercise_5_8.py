# exercise 5-8 login
# list of usernames one user called admin
# generic greeting for non-admin users
# special greeting for admin
users = ['Jackson', 'Aaron', 'admin', 'Amelia', 'Sarah', 'Shawn']

for user in users:
    if user == 'admin':
        print(f'Hello {user}, enjoy your total controll of everything.')
    else:
        print(f'Hello {user}, welcome back.')
