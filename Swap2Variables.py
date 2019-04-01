a = 5
b = 6

print('value of a is %d' %a)
print('value of b is %d' %b)

a = a ^ b
b = a ^ b
a = a ^ b

print('swapped value of a is %d' %a)
print('swapped value of b is %d' %b)

a,b = b,a

print('swapped value of a is %d' %a)
print('swapped value of b is %d' %b)