# exercise 5-5 if else chain
# not the expected implementation, but, it'll do.
def print_score(alien_color: str):
    if alien_color == 'green':
        print('+5 pts.')
    elif alien_color == 'yellow':
        print('+10 pts.')
    else:
        print('+15 pts.')


print_score('green')
print_score('red')
print_score('yellow')
