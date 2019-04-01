# number divisible by 1 and itself is called prime number

not_prime_nums = [j for i in range(2,50) for j in range(i*2,50,i)]
prime_nums = [j for j in range(2,50) if j not in not_prime_nums]
print prime_nums

name = 'Dhanasekaran'
l={}

for i in range(name.__len__()):
    l
print l.keys()