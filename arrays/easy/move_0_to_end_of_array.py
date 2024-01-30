nums = [1, 0, 3, 0, 5, 0, 7]
i = 0
for num in nums:
    if num != 0:
        nums[i] = num
        i += 1

while i < len(nums):
    nums[i] = 0
    i += 1

print(nums)

