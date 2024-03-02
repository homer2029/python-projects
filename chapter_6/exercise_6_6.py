# exercise 6-6 favorite languages poll
# list of people who should be polled
# dictonary of people who have been polled
# print thanks to people who have been polled
# encourage people who haven't to vote
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'rust', 'phil': 'python'}

voters = ['jackson', 'amelia', 'aaron', 'jen', 'sarah', 'edward', 'phil']

# sorting is NOT required here...
for voter in sorted(voters):
    if voter in favorite_languages.keys():
        print(f'Thank you for voting {voter.title()}. Your vote counts.')
    else:
        print(f'{voter.title()} we still need your vote!')
