########################################
Generator function runs only once and also remembers its last position
########################################

def Generate():
    for j in range(5):
        yield (j*j)

for k in Generate():
    print(k)
