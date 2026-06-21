import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow
}


def calc(expression):

    op, x, y = expression.split()

    x = float(x)
    y = float(y)

    return operations[op](x, y)

print(calc('** 2 4'))