

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

