# exercise 7-10 dream vacation
# poll users to enter their user name and where they want to go on vacation
# users may choose to continue or exit the poll
# print the results at the end
import re

continue_prompt = 'Are there others to poll? ((y)es/(n)o)'

# nothing in this function is strictly required.


def continue_poll(keep_polling: str) -> bool:
    # not the perfect regex solution, but it keeps some of the riff-raff out :)
    y_n_yes_no_pattern = '^(yes)|y|(no)|n$'
    while not re.search(y_n_yes_no_pattern, keep_polling):
        keep_polling = input(continue_prompt)

    return 'y' == keep_polling.lower() or 'yes' == keep_polling.lower()


print('***Dream Vacation Poll***')

name_prompt = 'Please enter your name: '
vacation_prompt = 'Where would you like to go for a dream vacation? '

results = {}

while True:
    person = input(name_prompt)
    destination = input(vacation_prompt)
    keep_polling = input(continue_prompt)
    results[person] = destination
    print()
    if not continue_poll(keep_polling):
        break

print('---Dream Vacation Poll Results---')
print()
for person, destination in results.items():
    print(f"{person.title()}'s dream vacation is to: {destination.title()}.")
