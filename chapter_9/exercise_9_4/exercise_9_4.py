# exercise 9-4 number served
# start with the restaurant from exercise 9-1
# add the attribute number served
# print restaurant num served, edit value, and print again
# also add set num served and increment num served.
from restaurant import Restaurant

london_calling = Restaurant('london calling', 'pub food')
print('Before')
london_calling.describe_restaurant()
london_calling.number_served = 500
print('After')
london_calling.describe_restaurant()

niji = Restaurant('niji', 'hibachi grill and sushi')
print('Before')
niji.describe_restaurant()
niji.set_number_served(-1)
niji.set_number_served(43)
print('After')
niji.describe_restaurant()
niji.set_number_served(42)

taj_mahal = Restaurant('taj mahal', 'indian')
print('Before')
taj_mahal.describe_restaurant()
taj_mahal.set_number_served(23)
taj_mahal.increment_number_served(0)
taj_mahal.increment_number_served(-53)
taj_mahal.increment_number_served(105_639)  # num served = 105662
print('After')
taj_mahal.describe_restaurant()
