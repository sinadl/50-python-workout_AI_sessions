movies = [
    ("Oppenheimer", 180, "Christopher Nolan"),
    ("Barbie", 114, "Greta Gerwig"),
    ("Killers of the Flower Moon", 206, "Martin Scorsese"),
    ("Poor Things", 141, "Yorgos Lanthimos"),
    ("The Holdovers", 133, "Alexander Payne"),
    ("American Fiction", 117, "Cord Jefferson"),
    ("Anatomy of a Fall", 151, "Justine Triet"),
    ("Past Lives", 105, "Celine Song"),
    ("The Zone of Interest", 105, "Jonathan Glazer"),
    ("Maestro", 129, "Bradley Cooper"),
]

sort_based = input('what field do you want to sort list?')

def sort_movies(sort_item):
    if sort_item == 'name':
        return sorted(movies, key=lambda x: (x[0]))
    elif sort_item == 'duration':
        return sorted(movies, key=lambda x: (x[1]))
    elif sort_item == 'director':
        return sorted(movies, key=lambda x: (x[2]))
        

for p in sort_movies(sort_based):
    print(f"{p[0]}, {p[1]}, {p[2]}")
