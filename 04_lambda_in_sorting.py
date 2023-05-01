x = [(4, 'b'), (2, 'a'), (5, 'c'), (1, 'e'), (3, 'd')]

# by default the sorting key is the first element in each toupl:

print(sorted(x))

# using lambda to change the key of sorting

print(sorted(x, key= lambda i: i[1]))