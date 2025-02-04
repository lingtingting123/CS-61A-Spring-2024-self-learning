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
