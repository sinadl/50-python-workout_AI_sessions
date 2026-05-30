def combine_dicts(dicts):
    result = {}

    for d in dicts:
        for k, v in d.items():
            if k not in result:
                result[k] = v
            else:
                if not isinstance(result[k], list):
                    result[k] = [result[k]]
                result[k].append(v)

    return result

lst = [
    {"a": 1, "b": 2},
    {"a": 10, "c": 3},
    {"b": 20}
]

print(combine_dicts(lst))
