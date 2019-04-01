'''
selection sort takes the first element in a list and compares with other elements in list
if a minimum value is found, its swapped at the first position.
'''
def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


nums = [5,3,8,6,7,2]

sort(nums)
print(nums)