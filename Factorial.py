# Factorial is multiple the number with each -1 than previous number
# Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120


def Factorial(n):
    f = 1
    for n1 in range(1,n + 1):
        f = f * n1

    return f

result = Factorial(5)

print(result)