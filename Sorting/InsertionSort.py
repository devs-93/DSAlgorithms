def insertion_sort(A):
    for i in range(1, len(A)):
        comp_value = A[i]
        position = i
        while position > 0 and A[position - 1] > comp_value:
            A[position] = A[position - 1]
            position=position-1
        A[position]=comp_value



data_list = eval(input())
insertion_sort(data_list)
print(data_list)
