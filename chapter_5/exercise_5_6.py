# stages of life
# < 2 -> baby
# 2 - 4 -> toddler
# 4 - < 13 -> kid
# 13 - 19 -> teenager
# 20 - 65 -> adult
# 65 or older -> elder
def get_life_stage(age :int):
    if age < 2:
        return 'baby'
    elif age >= 2 and age < 4:
        return 'toddler'
    elif age >= 4 and age < 13:
        return 'kid'
    elif age >= 13 and age < 20:
        return 'teenager'
    elif age >= 20 and age < 65:
        return 'adult'
    elif age >= 65:
        return 'elder'

# more robust example, you get the idea        
print(f'Amelia age 11 is a(n) {get_life_stage(11)}.')
print(f'Jackson age 14 is a(n) {get_life_stage(14)}.')
print(f'Aaron age 43 is a(n) {get_life_stage(43)}.')
print(f'Sarah age 43 is a(n) {get_life_stage(43)}.')
print()
for age in range(0, 70):
    print(f'{age} -> {get_life_stage(age)}')