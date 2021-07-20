from math import floor


def binary_search(list, key):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle_element = floor((left + right) / 2)
        if list[middle_element] == key:
            return middle_element
        elif list[middle_element] < key:
            left = middle_element + 1
        elif list[middle_element] > key:
            right = middle_element - 1
    return -1


data_list = eval(input())
key = int(input())
result = binary_search(data_list, key)
print(result)
