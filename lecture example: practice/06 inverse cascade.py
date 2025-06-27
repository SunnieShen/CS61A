"inverse cascade"

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow=lambda n: f_then_g(grow(n//10),print(n),n)
shrink=lambda n: f_then_g(print(n),grow(n//10,n))

"another version"
def grow(n):
    grow(n//10)
    #no return statment, otherwise the function ends
    print(n)
def shrink(n):
    print(n)
    grow(n//10)


"counting partitions"
def count_partitions(n,m):
    if n<0 or m==0: return 0
    elif n==0: return 1
    #no object>>> partition method=1, not 0
    else:
        with_m=count_partitions(n-m,m)
        without_m=count_partitions(n,m-1)
        return with_m + without_m