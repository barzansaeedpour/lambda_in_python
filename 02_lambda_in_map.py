
x = [1,2,3,4,5,6,7,8,9,10]

# a simple usecase of map:

def multi(i):
    return i * i

print(list(map(multi, x)))

# doing the same thing using lambda:

multi = lambda i: i*i
print(list(map( multi, x)))

# or:

print(list(map(lambda i: i*i, x)))




