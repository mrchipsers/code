def eggs(n):
    #boxes=-(n//-6)
    boxes = (n+5)//6
    #or
    #empty=-(n%-6)
    empty=(boxes*6)-n
    #empty = (6-(n%6))%6
    if boxes<2:
        box= "there is 1 box"
    else:
        box= f"there are {boxes} boxes"
    if empty==1:
        am= "there is 1 empy spot in the last box"
    else:
        am= f"there are {empty} empty spots in the last box"
    return f"for {n} eggs {box}, and {am}"
#egg=int(input("please input a number of eggs: "))
#print(eggs(egg))
for i in range(5,15):
    print(eggs(i))