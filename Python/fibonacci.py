def make_fibonacci(n: int):
    flist=[]  
    for i in range(n):
        if i==0:
            flist=[0]
        elif i==1:
            flist.append(1)
        else:
            flist.append(flist[-1]+flist[-2])
    return flist
for i in range(10):
    print(make_fibonacci(i))