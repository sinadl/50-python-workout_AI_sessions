def reverse_dic(items):
    return {items[keys]:keys for keys in items}


print({'a':1, 'b':2, 'c':3})
print(reverse_dic({'a':1, 'b':2, 'c':3}))