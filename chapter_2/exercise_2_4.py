# exercise 2-4 changing the case of strings
person = 'jAcKsOn DAviD mIllS'
print(person.lower())
print(person.upper())
print(person.title())
# The actual value for person is unchanged when calling these string casing methods; but the value
# returned can be re-assigned like person = person.lower()
print(person)
# This wasn't required, just curious as to what it did
print(person.casefold())