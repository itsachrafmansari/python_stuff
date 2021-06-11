i = 0  # Counting checked cases
n = 3  # To the power of
limit = 100  # Max value for X, Y and Z (the number of cases = limit ** 3)

for x in range(1, limit + 1):
    for y in range(1, limit + 1):
        for z in range(1, limit + 1):
            if (x ** n) + (y ** n) == (z ** n):
                print('{0} ^ {3}  +  {1} ^ {3}    =    {2} ^ {3}'.format(x, y, z, n))
            i += 1

print(i)
