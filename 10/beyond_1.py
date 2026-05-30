def mysum_bigger_than(*items):
    if not items:
        return items
    
    threshold = items[0]
    output = None
    for item in items[1:]:
        if threshold < item:
            if output:
                output += item
            else:
                output = item
        
        
    return output

print(mysum_bigger_than("m", "apple", "zoo", "moon", "cat"))