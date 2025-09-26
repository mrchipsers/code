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
n=int(input("how many numbers of the fibonacci sequence do you want generated?"))
print(make_fibonacci(n))