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

"""discussion04"""
def path(x,y,m,n):
    # if x > m or y > n:
    #     return 0 
    # if x == m and y == n:
    #     return 1
    if x == m or y == n: #碰到边界的情况+没碰到边界的情况到达终点
        return 1
    return path(x + 1,y,m,n) + path(x,y + 1,m,n)
  

