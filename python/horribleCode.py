def where(price: list, retail: list):
    new=[]
    for i in price:
        avg=sum(retail)/len(retail)
        if i>avg:
            new.append(i)
    return new
price=[]
retail=[]
avg=sum(retail)/len(retail)
new=[i for i in price if i>avg]