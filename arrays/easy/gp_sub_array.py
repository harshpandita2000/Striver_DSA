def max_subarray_length(arr, target_sum):
    sum_indices = {}  # Dictionary to store cumulative sum and its corresponding index
    max_length = 0
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum == target_sum:
            max_length = i + 1

        if current_sum not in sum_indices:
            sum_indices[current_sum] = i
        else:
            max_length = max(max_length, i - sum_indices[current_sum - target_sum])

    print(max_length)
arr = [0, 1 ,1, -1 ,-1, 0]
max_subarray_length(arr, 0)