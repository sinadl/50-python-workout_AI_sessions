class MyEnumerate:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator)
        result = (self.index, value)
        self.index += 1
        return result
    
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')