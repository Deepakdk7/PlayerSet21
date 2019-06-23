ax=list(input())
for i in ax:
    if i.islower()==True:
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
