pos = -1
def search(list, n):
    list.sort()
    print(list)
    l = 0
    u = len(list) - 1

    while l <= u:
        m = (l + u) // 2

        if list[m] == n:
            globals()['pos']  = m
            return True
        else:
            if list[m] < n:
                l = m + 1
            else:
                u = m - 1
    return False

n = 210
list = [4,3, 9, 21, 15,13, 17]

if search(list,n):
    print('number found at ', pos)
else:
    print 'number not found'