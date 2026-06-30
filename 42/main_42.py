class FlexibleDict(dict):

    def __getitem__(self, key):

        try:
            return super().__getitem__(key)

        except KeyError:
            pass

        try:
            return super().__getitem__(str(key))

        except KeyError:
            pass

        try:
            return super().__getitem__(int(key))

        except (KeyError, ValueError):
            pass

        raise KeyError(key)
    
    
fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])
fd[5] = 500
print(fd[5])
fd[1] = 100
print(fd['1'])
fd['1'] = 100
print(fd[1])