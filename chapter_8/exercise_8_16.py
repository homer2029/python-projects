# exercise 8-16 imports
# use a function from a previous exercise and import it in all the ways
from exercise_8_8 import *
import exercise_8_9 as ex89
from exercise_8_12 import make_sandwich as ms
from exercise_8_11 import send_messages
import exercise_8_12

sandwich = exercise_8_12.make_sandwich('peanut butter', 'jelly')
print(sandwich)


send_messages(['hello world'], [])


new_sandwich = ms('turkey', 'ham', 'provalone',
                  'oregano and basil', 'oil and vinegar')
print(new_sandwich)


ex89.show_messages(['some message', 'some other message'])


main_pgm_loop()
