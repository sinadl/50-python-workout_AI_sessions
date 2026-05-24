# beyond 1
def run_timing(flt,before,after):
    s = str(flt)
    two_part = s.split('.')

    bef = two_part[0][-before:]
    aft = two_part[1][:after]

    return float(f"{bef}.{aft}")
print(run_timing(1245.51203213,2,4))

# beyond 2
from decimal import Decimal 
def decimal_problem(flt1,flt2):
    d1 = Decimal(flt1)
    d2 = Decimal(flt2)
    return(float(d1+d2),float(flt1)+float(flt2))

print(decimal_problem('0.1','0.2'))