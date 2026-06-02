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

sort_based = input('what field do you want to sort list?(more than 1 one choice)')

def sort_movies(sort_item):
    sort_list = sort_item.split(',')
    sort_number=[]
    for item in sort_list:
        if item == 'name': sort_number.append(0)
        elif item == 'duration': sort_number.append(1)
        elif item == 'director': sort_number.append(2)
    
    return sorted(movies, key=lambda x: tuple(x[i] for i in sort_number))

        

for p in sort_movies(sort_based):
    print(f"{p[0]}, {p[1]}, {p[2]}")
