res = 0;
for x in range(0, 1000):
    if x%3 ==0 or x%5==0:
        res += x
print(res, x)




""" the following code is for ugly number problem
res = []
i3=0
i5=0
res.append(1)
next3=res[i3]*3
next5=res[i5]*5
while res[-1] < 10:
    tmp = min(next3, next5)
    if tmp>10:
        break
    res.append(tmp)
    if tmp == next3:
        i3+=1
        next3 = res[i3]*3
    else:
        i5+=1
        next5 = res[i5]*5
sumres=0;
for x in res:
    sumres += x;
print (res);
"""
