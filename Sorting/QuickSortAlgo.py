def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right
    while True:
        while i <= j and arr[i] < pivot:
            i = i + 1
        while i <= j and arr[j] >= pivot:
            j = j - 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[j], arr[left] = arr[left], arr[j]
    return j


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


data_list = eval(input())
quick_sort(data_list,0,len(data_list)-1)
print(data_list)
