# Q1: Big Fib
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

"""
complete the expression below by writing only names and parentheses in the blanks 
so that it evaluates to the smallest Fibonacci number that is larger than 2024.
"""
next(filter(lambda n: n > 2024, gen_fib()))


# Q2: Something Different
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    cur_elem = next(t)
    for next_elem in t:
        yield next_elem - cur_elem
        cur_elem = next_elem



# Q3: Partitions
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for part in partition_gen(n - m, m):
            yield part + '+' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield partition_gen(n,m - 1)