import math
ax=int(input())
for i in range(0,ax+1):
    print((math.factorial(2*i))//((math.factorial(i+1))*(math.factorial(i))),end=' ')
