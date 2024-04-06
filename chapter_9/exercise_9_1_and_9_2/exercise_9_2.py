# exercise 9-2 three restaurants
# make three restaurants and call describe restaurant on all three instances
# sigh...
from restaurant import Restaurant as R

res_1 = R('the grotto', 'new californian cusine')
res_2 = R('taj mahal', 'indian')
res_3 = R('grad school', 'greasy spoon')

res_1.describe_restaurant()
res_2.describe_restaurant()
res_3.describe_restaurant()
