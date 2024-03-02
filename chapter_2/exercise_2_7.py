# exercise 2-7 strip
str = '\n\tHello\n\tWorld  .  '
print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())

# perhaps a better example of strip()
str = '    blah   '
print(f'blah {str} blah.')
print(f'blah {str.strip()} blah.')
print(f'blah {str.lstrip()} blah.')
print(f'blah {str.rstrip()} blah.')