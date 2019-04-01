'''
Iterators are used to loop an iterable but one item at a time
each time it remember the last value and gives the next value
'''

#lst = [5,9,3,1,7]

#it = iter(lst)

#print (it.next())
#print (it.next())

# own iterator

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.num <= 10):
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)
