def my_recursion(n):
    print(n)
    if n == 3:
        return
    my_recursion(n+1)
    my_recursion(n+1)


# my_recursion(1)

def get_fib(num):
    two_behind = 0
    one_behind = 1
    for integer in range(1, num):
        two_behind, one_behind = one_behind, one_behind + two_behind
    print(one_behind)


get_fib(10)


def fib(n):
    f0 = 0
    f1 = 1
    for i in range(1, n):
        fn = f1 + f0
        f0 = f1
        f1 = fn
    return(fn)


print(fib(10))
