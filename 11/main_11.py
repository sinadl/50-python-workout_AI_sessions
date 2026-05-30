PEOPLE = [
    {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
    {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
]

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=lambda person: (person['last'], person['first']))

print(alphabetize_names(PEOPLE))


import operator

def alphabetize_names_1(list_of_dicts):
    return sorted(list_of_dicts,key=operator.itemgetter('last', 'first'))

print(alphabetize_names_1(PEOPLE))