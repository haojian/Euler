res = 0
fib1 = 1
fib2 = 2
while (fib2 < 4000000):
    if fib2%2 ==0:
        res+= fib2
    tmp = fib1
    fib1 = fib2
    fib2 = fib1+tmp
print(res, fib1)
