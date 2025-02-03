def parabola(x):
    return (x-3) * (x-6)

def vee(x):
    return abs(x-2)

def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee)
    3
    """
    n = 1
    while 1:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m += 1
        n += 1
    
        