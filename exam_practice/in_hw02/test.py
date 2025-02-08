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
         

