def square(x):
    return x * x

def search(f):
    x = 0
    while True:
        if f(x) == True:
            return x
        x += 1

def is_three(x):
    return x == 3

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow,print,n//10)
shrink = lambda n: f_then_g(print,shrink,n//10)

"""
Trees videos
count paths that have a total label sum
"""
def count_paths(t,total):
    if total == label(t):
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b,total - label(t)) for b in branches(t)])

class Link:
    empty = ()
    def __init__(self,first,rest=empty):
        self.first = first
        self.rest = rest

def add(s,v):
    if s == Link.empty:
        return Link(v)
    if v == s.first:
        return s
    if v > s.first:
        return Link(s.first,add(s.rest,v))
    if v < s.first:
        return Link(v,s)

def prune(t,n):
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b,n)


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    
def max_product(s): # 
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if s == []:
        return 1
    else:
        return max(s[0] * max_product(s[2:]),max_product(s[1:]))

def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"
    if s == []:
        return
    s[0] = f(s[0])
    for i in range(1,len(s)):
        if type(s[i]) == list:
            deep_map(f,s[i])
        else:
            s[i] = f(s[i])


def make_change(amount, coins):
    """Return a list of coins that sum to amount, preferring the smallest coins
    available and placing the smallest coins first in the returned list.

    The coins argument is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if not coins:
        return None
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    if amount < smallest:
        return None
    "*** YOUR CODE HERE ***"
    if amount == smallest:
        return [smallest]
    list = make_change(amount - smallest,rest)
    # while not list:
    #     if not rest:
    #         return None
    #     smallest = min(rest)
    #     rest = remove_one(rest, smallest)
    #     print('DEBUG:',"try again",smallest)
    #     list = make_change(amount - smallest,rest)
    # return [smallest] + list
    if not list:
        return make_change(amount,rest)
    return [smallest] + make_change(amount - smallest,rest)