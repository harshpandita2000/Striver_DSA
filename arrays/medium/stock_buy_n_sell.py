def stock(arr):
    n=len(arr)
    maxx=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                maxx =max(maxx,arr[j]-arr[i])
    return maxx

arr= [7,6,4,3,1]
print(stock(arr))

