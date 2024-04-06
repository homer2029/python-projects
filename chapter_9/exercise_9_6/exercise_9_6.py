# exercise 9-6 ice cream stand
# new class, ice cream stand a sub-type of restaurant
# ice cream stand has a prop called flavors that takes a list of strings
# and a method that displays the flavors
# create and ice cream stand and call the display flavors method
from ice_cream_stand import IceCreamStand

andys = IceCreamStand(
    "andy's", ['vanilla', 'chocolate', 'cookies and cream', 'strawberry'])


andys.describe_restaurant()

andys.open_restaurant()

print()

andys.display_flavors()
