def mysum(*args):
    sumv = 0
    for i in args:
        sumv +=i
    print(sumv)

mysum(5,2,6,3)


# beyond 1

def mysum(*args,start):
    sumv=0
    try:
        sumv += start
    except ValueError:
        print(f"Invalid input! Please enter a valid number for base {start}.")

    for i in args:
        sumv +=i
  

mysum(5,2,6,3,start=20)

# beyond 2

def mysum_avg(*args):
    sumv=0
    for i in args:
        sumv +=i
    sumv = sumv / len(args)
    return sumv


print(mysum_avg(4,5,2))

# beyond 3

def mysum_minmax(*args):
    len_minmax = [len(i) for i in args]
    min_len = min(len_minmax)
    max_len = max(len_minmax)
    avg_len = sum(len_minmax)/len(args)
    return min_len,max_len,avg_len


print(mysum_minmax('book','apple','heisenberg'))