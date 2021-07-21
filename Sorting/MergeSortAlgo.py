def merge_algo(A, left, middle_element, right):
    i=left
    j=middle_element+1
    k=left
    B=[None]*(right+1)
    while i<=middle_element and j<=right:
        if A[i]<A[j]:
            B[k]=A[i]
            i=i+1
        else:
            B[k]=A[j]
            j=j+1
        k = k + 1
    while j<=right:
        B[k]=A[j]
        k=k+1
        j=j+1
    while i<=middle_element:
        B[k]=A[i]
        k=k+1
        i=i+1

    for x in range(left,right+1):
        A[x]=B[x]


def merge_sort(A, left, right):
    if (left < right):
        middle_element = (left + right) // 2
        merge_sort(A, left, middle_element)
        merge_sort(A, middle_element + 1, right)
        merge_algo(A, left, middle_element, right)


data_list = eval(input())
merge_sort(data_list,0,len(data_list)-1)
print(data_list)
