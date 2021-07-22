def count_sort(s_array):
    max_element=max(s_array)
    c_array= [0] * (max_element + 1)
    for i in range(0, len(s_array)):
        c_array[s_array[i]]= c_array[s_array[i]] + 1
    i=0 # traversing count list
    j=0 # 
    size_of_count_arr=max_element+1
    while i < size_of_count_arr:
        if c_array[i]>0:
            s_array[j]=i
            c_array[i]= c_array[i] - 1
            j=j+1
        else:
            i=i+1





data_list = eval(input())
count_sort(data_list)
print(data_list)