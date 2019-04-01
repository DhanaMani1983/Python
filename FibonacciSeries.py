# add first number and second number to get the third number
# 0 1 1 2 3 5 8 13 21 34
# In above sequence 0 + 1 = 1 1 + 1 =2 1 + 2 = 3

def fibonacci(n):
    a = 0
    b = 1
    if (n<0):
        print('Invalid Number')
    elif(n==1):
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            if (b>n):
                break
            print(b)

fibonacci(100)