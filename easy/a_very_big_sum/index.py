def a_very_big_sum(arr):
    sum_of_arr=0
    for ar in arr:
        sum_of_arr=sum_of_arr+ar
    return sum_of_arr


print(a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))