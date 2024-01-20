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
# tc:O(N^2)
# sc:O(1)
#DNF ALGO APPROACH
def sort(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return(arr)

arr=[0,0,0,1,2,1,1,0]
print(sort(arr))
# TC:O(N)
# SC:O(1)