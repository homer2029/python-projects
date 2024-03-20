# exercise 9-2 three resturants
# make three resturants and call describe resturant on all three instances
# sigh...
from resturant import Resturant as R

res_1 = R('the grotto', 'new californian cusine')
res_2 = R('taj mahal', 'indian')
res_3 = R('grad school', 'greasy spoon')

res_1.describe_resturant()
res_2.describe_resturant()
res_3.describe_resturant()
