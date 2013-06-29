num = 600851475143 
res = 1
maxfac = 1
while maxfac <= num:
    if num%maxfac == 0:
        num /= maxfac
        res = maxfac
    maxfac+=1
print(res)
