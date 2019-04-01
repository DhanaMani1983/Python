'''
using decorators we can add extra features to existing functions
say if you have divsion function which divides two numbers
logic is you want the largest number to be numerator all the time you can
use decorators
'''

def div(a,b):
    print (a/b)

def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,8)

