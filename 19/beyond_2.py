numbers = [int(n) for n in input("Enter integers separated by spaces: ").split()]

factors_dict = {}

for num in numbers:
    for factor in range(1, num + 1):
        if num % factor == 0:
            factors_dict.setdefault(factor, []).append(num)

print(factors_dict)