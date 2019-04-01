#filter

nums = [1,4,7,9,2,8,3,5,6]

def is_even(n):
    return n%2 == 0

evens = filter(is_even,nums)

print(evens)

# using lambda

nums = [1,4,7,9,2,8,3,5,6]

odds = filter(lambda n:n%2==1,nums)

print(odds)


doubles = map(lambda n : n + 2, evens)

print(doubles)

sum = reduce(lambda a,b : a + b, doubles)
print(sum)