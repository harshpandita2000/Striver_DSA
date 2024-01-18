
#2nd optimisation avoid using temp arr
def sum_k(arr, k):
    arr_sum = 0
    leng=0
    i = 0
    j = 0
    n = len(arr)                         
    while i < n:                   
        j = i
        arr_sum = 0
        while j < n:
            arr_sum += arr[j]
            if arr_sum == k:
               # sub_arr.append(temp)
                leng=max(leng, j - i + 1)
            j += 1
        i += 1
    print(leng)
    
#arr = [17, 0, 0, 0, 0, 17, 0, 0]
arr = [17, 0, 0, 0, 0, 17, 0, 0, -1,1]
sum_k(arr, 17)
#TC:O(N) #BECAUSE  inner loop efficiently traverses the array only once,while outer loop runs n times
#SC:O(1)


#sliding wind approach
def sum_k_optimized(arr, k):
    n = len(arr)
    arr_sum = 0
    start = 0
    leng = 0

    for end in range(n):
        arr_sum += arr[end]

        while arr_sum > k:
            arr_sum -= arr[start]
            start += 1

        if arr_sum == k:
            leng = max(leng, end - start + 1)

    return leng
arr=[8, 15, 17, 0, 11]
print(sum_k_optimized(arr, 17))










