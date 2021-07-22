def bubble_sort(A):
    n = len(A)
    for j in range(0, n - 1):
        #reducing the no of compairsion while sorting
        for i in range(0, n - 1 - j):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp


data_list = eval(input())
bubble_sort(data_list)
print(data_list)
