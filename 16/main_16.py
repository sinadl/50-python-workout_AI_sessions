def dictdiff(first,second):
    output = {}
    con_cat = first.keys() | second.keys()
    
    for i_keys in con_cat:
        if first.get(i_keys) != second.get(i_keys):
            output[i_keys] = [first.get(i_keys),second.get(i_keys)]
    
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