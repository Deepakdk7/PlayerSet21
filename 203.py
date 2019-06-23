ax=int(input())
d=[]
a=[]
for i in range(0,ax):
    a.append(list(input()))
for i in a:
    c=0
    for j in range(0,len(i)):
        if i[j]=='a' or i[j]=='e' or i[j]=='i' or i[j]=='o' or i[j]=='u':
            c=c+1
    d.append(c)
x=dict(zip(d,a))
d.sort()
d=d[::-1]
for i in d:
    print(*x[i],sep='')
