def name_triangle():
    source_name = input('Enter your choosen name here:')
    for place,letter in enumerate(source_name):
        print(source_name[:place])
    
name_triangle()