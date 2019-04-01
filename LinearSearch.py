pos = -1
def search(list,n):
    i = 0

    while(i < len(list)):
        if list[i] == n:
            globals()["pos"] = i
            return True
        i += 1
    return False

def search1(list, n):
    for i in range(len(list)):
        if list[i] == n
            return True
    return False

list = [5,3,4,2,9,7,6]

n = 7

if search(list,n):
    print ("number found at %d" %pos)
else:
    print "number not found"

