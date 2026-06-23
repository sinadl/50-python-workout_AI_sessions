def flatten(numbers):
    
    return [x for y in numbers for x in y]


print(flatten([[1,2], [3,4]]))