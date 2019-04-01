from __future__ import print_function
for i in range(4):
    for j in range(4-i):
        print(j+i+1,end="")
    print()

str1 = 'ABCD'
str2 = 'PQR'
for x in range(4):
    print(str1[:x+1] + str2[x:])