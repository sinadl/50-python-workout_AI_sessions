def dict_partition(d, f):
    true_dict = {}
    false_dict = {}

    for key, value in d.items():
        if f(value):
            true_dict[key] = value
        else:
            false_dict[key] = value

    return true_dict, false_dict


def greater_than(item):
    return item > 10

data = {
    "a": 5,
    "b": 20,
    "c": 8,
    "d": 15
}
print(dict_partition(data,greater_than))