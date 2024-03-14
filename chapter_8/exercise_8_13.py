# exercise 8-13 user profile
# start from user_profile.py from p 148 in book
# make a user profile and pass at least 3 kwargs
# the below code is 1 to 1 user_profile.py
def build_profile(first, last, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


# my code... so challenging...
user_profile = build_profile(
    'albert', 'pujols', team='cardinals', position='first base', slugging='.544')

print(user_profile)
