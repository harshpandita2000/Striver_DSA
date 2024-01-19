def sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] >= arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return(arr)
# arr=[1,0,0,1,2,1]
arr=[0,0,0,1,2,1,1,0]
print(sort(arr))


