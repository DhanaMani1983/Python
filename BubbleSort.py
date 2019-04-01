'''
compares consecutive elements and swaps the min and max values
'''
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


nums = [5,3,8,6,7,2]
sort(nums)
print(nums)