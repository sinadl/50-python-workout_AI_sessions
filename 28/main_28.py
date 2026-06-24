def join_numbers(numbers):
    return ','.join([str(x) for x in numbers])


print(join_numbers(range(15)))