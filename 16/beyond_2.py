def make_dict(*args):
    result = {}

    for i in range(0, len(args), 2):
        key = args[i]
        value = args[i+1]
        result[key] = value

    return result


print(make_dict('a', 1, 'b', 2, 'c', 3))