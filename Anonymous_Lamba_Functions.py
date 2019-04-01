# lambda can take multiple arguments but needs to have only one expression
def square(n):
    return n*n


result = square(5)

print(result)

func = lambda a : a * a

result = func(11)

print(result)