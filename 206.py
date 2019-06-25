try:
    a=input()
    a=int(a,16)
    a=str(a)
    if a.isnumeric()==True:
        print('yes')
except:
    print('no')
