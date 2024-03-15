# exercise 8-14 cars
# make a function that accepts manufacture and model plus an
# arbitrary number of key value arguments and returns a dictionary
# print the dictionary
def build_car_info(manufacturer: str, model: str, **info) -> dict[str, str]:
    """Builds a car info dictionary. Accepts kwargs.

    Args:
        manufacturer (str): The manufacturer of the car.
        model (str): The model of the car.
        info: Any additional info about the car.

    Returns:
        dict[str,str]: The car info dictionary.
    """
    info['manufacturer'] = manufacturer.capitalize()
    info['model'] = model.upper()
    return info


car_info = build_car_info(
    'subaru', 'impreza', color='blue', doors=4, sun_roof=True)
car_info_2 = build_car_info('nissan', '350z')

print(car_info)
print(car_info_2)

for car in [car_info, car_info_2]:
    print()
    for info, val in car.items():
        print(f'{info} -> {val}')
