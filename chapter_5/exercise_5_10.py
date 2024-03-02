# exercise 5-10 checking usernames
# two lists new users and current users
# check that all new users are in current users
# print an error message for the repeated user names
# case insensitve compare
current_users = ['BoxKing', 'homer', 'UniGirl',
                 'isabella', 'amills', 'ella', 'TurTle']
new_users = ['Megan427', 'caLipso', 'bOxkIng', 'paloma', 'pally', 'ELLA']
current_users_copy = []

print(current_users)

for current_user in current_users:
    current_users_copy.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f'Username: {new_user} already exists. Choose a new name.')
    else:
        current_users.append(new_user)

print()
print(current_users)
