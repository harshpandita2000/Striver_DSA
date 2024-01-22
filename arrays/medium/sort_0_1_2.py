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

arr=[0,2,0,1]
print(sort(arr))
# TC:O(N)
# SC:O(1)


def sort(arr):
    n = len(arr)
    arr2 = []
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(0,n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 2:
            cnt2 +=1
        else:
            cnt1 +=1
    #print(cnt0,cnt1,cnt2)
    for i in range(cnt0):
        arr2.append(0)
    for i in range(cnt1):
        arr2.append(1)
    for i in range(cnt2):
        arr2.append(2)
    
    return(arr2)

arr=[0,0,0,1,2,1,1,0]
print(sort(arr))