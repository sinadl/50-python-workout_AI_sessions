def sum_numbers(numbers):
    
    return sum(int(x) for x in numbers.split() if x.isdigit())


print(sum_numbers('10 abc 20 de44 30 55fg 40'))