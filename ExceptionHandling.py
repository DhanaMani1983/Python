'''
Create the code within try catch block

'''

a = 5
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:
    print("denominator cannot be zero", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print(e)
finally:
    print("resource closed")
