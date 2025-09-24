print("please enter numbers separated by spaces: ")
list=input()
list=list.split()
list=[int(i) for i in list]
def sort(list):
    for i in range(len(list)):
        smallest_index=i
        for j in range(i,len(list)):
            if list[j]<list[smallest_index]:
                smallest_index=j
        list[i], list[smallest_index]= list[smallest_index],list[i]
    return list
print(sort(list))
#def smallest_to_largest(list):
#    c=0
#    while c<len(list):
#        swap_smallest(list,c)
#        c+=1
#    return list
#print(smallest_to_largest(list))