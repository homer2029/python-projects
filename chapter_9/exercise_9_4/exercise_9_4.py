# exercise 9-4 number served
# start with the restaurant from exercise 9-1
# add the attribute number served
# print restaurant num served, edit value, and print again
from restaurant import Restaurant

london_calling = Restaurant('london calling', 'pub food')
print('Before')
london_calling.describe_restaurant()
london_calling.number_served = 500
print('After')
london_calling.describe_restaurant()
