# exercise 8-15 printing_models.py with imports
# recreate the functionality of printing_models.py pg. 143
# move the functions to a a separate file and import them
from ex_8_15_external import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
