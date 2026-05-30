def mysum(*items):
    
    if not items:
        return items
    
    output = items[0]
    for item in items[1:]:
        output += item
        
    return output

#test case
print(mysum(23,41,51,32))