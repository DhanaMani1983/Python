# Recursion is calling the function within itself

import sys

print (sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print('Hello Dhana!', i)
    greet()

greet()