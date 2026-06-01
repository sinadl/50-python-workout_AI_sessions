import operator

PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in list_of_tuples:
        l_name= person[1]
        f_name= person[0]
        time = person[2]
        person_recombine = (l_name,f_name,time)

        print(template.format(*person_recombine))
        
format_sort_records(PEOPLE)
