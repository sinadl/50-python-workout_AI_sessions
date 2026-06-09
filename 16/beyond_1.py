def dictdiff(*items):
    output = {}
    con_cat = {}
    for item in items:
        for i_inner in item:
            output[i_inner] = item[i_inner]
                
    print(output)
    
    
    
d1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

d2 = {
    "a": 1,
    "b": 20,
    "d": 4
}
dictdiff(d1,d2)