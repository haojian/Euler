res = 0
for i in range(100,1000):
    for j in range(100, 1000):
        if(str(i*j) == str(i*j)[::-1]):
            res =max(res, i*j)
print(res)


"""
def palindromeCheck(n):
    digits=1
    tmp = n
    while( tmp >= 10):
        digits *=10
        tmp/=10
    leftscale = 1;
    while n>=10:
        r = int(n%10)
        l = int(n/digits)
        if r!=l:
            return False
        n -= l*digits + r
        n/=10
        digits/=100
        leftscale *=10
    return True
    


res = 0
for i in range(100,1000):
    for j in range(100, 1000):
        if(palindromeCheck(i*j)):
            res =max(res, i*j)
print(res)

"""
