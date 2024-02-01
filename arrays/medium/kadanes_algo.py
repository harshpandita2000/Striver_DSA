#kadane's algo
def maxsum_subarray(nums):
    sum = 0
    maxi = nums[0]
    for i in range(0,len(nums)):
        sum = sum + nums[i]
        maxi = max(sum,maxi)
        if sum < 0:
            sum = 0
    return maxi

arr =[-2,1,-3,4,-1,2,1,-5,4]
print(maxsum_subarray(arr))

#iterative approach
def maxsum(arr):
    maxi = arr[0]
    for i in range(0,len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            maxi = max(sum,maxi)
    return maxi
#arr =[-2,1,-3,4,-1,2,1,-5,4]
arr = [5,4,-1,7,8]
print(maxsum(arr))