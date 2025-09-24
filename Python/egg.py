def eggs(n):
    #boxes=-(n//-6)
    #boxes=((n+(6-1))//6)
    #empty=-(n%-6)
    #boxes=(n//6)+1 
    boxes = (n+5)//6
    #or
    #empty=(boxes*6)-n
    #empty=(boxes*6)-n
    #empty=empty%6
    empty = (6-(n%6))%6
    return f"there are {boxes} boxes, and {empty} spots in the last box"
egg=int(input("please input a number of eggs: "))
print(eggs(egg))
    