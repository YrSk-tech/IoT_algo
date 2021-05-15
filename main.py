def heapify(list,item,large):
    less=item
    left=item*2
    right=item*2+1

    if left<large and list[left]>list[less]:
        less=left

    if right < large and list[right] > list[less]:
        less = right

    if less!=item:
        list[item],list[less]=list[less],list[item]
        heapify(list,right,large)


def min_heap(list):
    n=len(list)

    for i in range(n,-1,-1):
        heapify(list,i,n)

    for i in range(n-1,0,-1):
        list[0],list[i]=list[i],list[0]
        heapify(list,0,i)

    return list

list_ex = [1,1]

print(min_heap(list_ex))
