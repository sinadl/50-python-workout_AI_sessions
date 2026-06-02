from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'email'])

PEOPLE = [
    Person('Reuven', 'Lerner', 'reuven@lerner.co.il'),
    Person('Donald', 'Trump', 'president@whitehouse.gov'),
    Person('Vladimir', 'Putin', 'president@kremvax.ru')
]

def alphabetize_names():
    return sorted(PEOPLE, key=lambda person: (person.last, person.first))

for p in alphabetize_names():
    print(f"{p.last}, {p.first}: {p.email}")
