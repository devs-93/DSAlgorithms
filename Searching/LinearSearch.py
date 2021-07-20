def linear_search(list,key):
    index=0
    while(index<len(list)):
        if list[index]==key:
            return index
        index=index+1
    return -1
arr=eval(input())
key=eval(input())
ind=linear_search(arr,key)
if ind:
    print("found ",ind)
else:
    print("not found")
