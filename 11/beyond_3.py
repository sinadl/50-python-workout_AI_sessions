def list_list_sort(numbers):
    return sorted(numbers, key=sum)

data = [
    [1, 2, 3],
    [10],
    [],
    [4, 4],
    [2, -1]
]

print(list_list_sort(data))

