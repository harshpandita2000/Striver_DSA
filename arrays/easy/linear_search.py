def linear_search(arr):
    for i in range(0,len(arr)):
        if arr[i]==item:
            return i
    return -1
    
arr=[1,4,7,5]
item=6
print(linear_search(arr))
