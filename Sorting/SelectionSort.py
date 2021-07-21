def selection_sort(A):
    for i in range(len(A)-1):
        position=i
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                position=j
        temp=A[position]
        A[position]=A[i]
        A[i]=temp
    return A

data_list = eval(input())
result = selection_sort(data_list)
print(result)
