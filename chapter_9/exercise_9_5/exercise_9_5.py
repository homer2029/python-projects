# exercise 9-5 login attempts
# modify exercise 9-3's user to add login_attempts
# add incriment and reset methods for login_attempts
# create a user and use the method several times
from user import User

user1 = User('aaron', 'mills', 43)

# should be 0
print(f'user1.login_attempts -> {user1.login_attempts}')
print('incrimenting login attempts for user1')

for n in range(0, 10):
    user1.incriment_login_attempts()

# should be 10
print(f'user1.login_attempts -> {user1.login_attempts}')
print('resetting login attempts for user1')

# should be 0
user1.reset_login_attempts()
print(f'user1.login_attempts -> {user1.login_attempts}')
