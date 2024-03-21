# exercise 9-3 users
# user class
# required props first name last name
# describe user method
# greet user method
# create multiple users
from user import User

user_1 = User('aaron', 'mills')
user_1.greet()
user_1.describe_user()

print()

user_2 = User('turks', 'andcaicos', 57, 'tac@molemail.bom', sea_view='yes')
user_2.greet()
user_2.describe_user()

print()

mario = User('mario', 'mario', email='mario@musroomk.in',
             age=40, favorite_color='red', favorite_saying="It's a me!")
mario.greet()
mario.describe_user()

print()

luigi = User(age=39, last_name='mario',
             first_name='luigi', favorite_color='green')
luigi.greet()
luigi.describe_user()
