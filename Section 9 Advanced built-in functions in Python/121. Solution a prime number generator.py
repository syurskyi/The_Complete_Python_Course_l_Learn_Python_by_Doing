def prime_generator(bound):
    for n in range(2, bound):  # n starts from 2 to bound
        for x in range(2, n):  # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:  # if no such x is found after exhausting all 1<x<n
            yield n  # generate this prime