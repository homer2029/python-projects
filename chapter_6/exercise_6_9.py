# exercise 6-9 favorite places
# dict key -> person; fav place -> value
favorite_places = {
    'aaron': 'paia, maui',
    'sarah': 'taos, new mexico',
    'mia': 'disneyland la, california'
}

for person, place in favorite_places.items():
    print(f"{person.title()}'s favorite place is: {place.upper()}.")
