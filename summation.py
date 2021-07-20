def sum_res(n):
    if n==0:
        return 0
    else:
        return n+sum_res(n-1)
print(sum_res(int(4)))