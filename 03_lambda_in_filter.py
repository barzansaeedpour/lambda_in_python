x = [1,2,3,4,5,6,7,8,9,10]

# a simple usecase of filter:

def even(i):

    if i % 2 == 0:
        return True
    else:
        return False

print(list(filter(even, x)))

# doing the same thing with lambda

even = lambda i: i%2 == 0
print(list(filter(even, x)))

# or:
print(list(filter(lambda i: i%2 == 0, x)))