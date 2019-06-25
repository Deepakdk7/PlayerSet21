ax=int(input())
a=[]
c=d=1
for i in range(0,ax):
    a.append(list(map(int,input().split())))
for i in range(0,len(a)):
    c=c*a[i][i]
i=0
j=len(a)-1
for n in range(0,len(a)):
    d=d*a[i][j]
    i=i+1
    j=j-1
print(c+d)
