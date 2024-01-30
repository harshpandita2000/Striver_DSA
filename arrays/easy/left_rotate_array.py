def left_rotate_array_by_one(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    return arr

arr=[1,2,3,4,5]
print(left_rotate_array_by_one(arr))