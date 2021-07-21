def binary_search_recur(list, key, left, right):
    if left > right:
        return -1
    else:
        middle_element = (left + right) // 2
        if list[middle_element] == key:
            return middle_element
        elif list[middle_element] < key:
            return binary_search_recur(list, key, (middle_element + 1), right)
        elif list[middle_element] > key:
            return binary_search_recur(list, key, left, (middle_element - 1))
    return -1


data_list = eval(input())
key = int(input())
l = 0
r = len(data_list) - 1
result = binary_search_recur(data_list, key, l, r)
print(result)
