def max_consecutive_one(arr):
    temp=[]
    cnt=0                       #1 1 0 1 1 1
    for i in range(0,len(arr)):
        if arr[i]==1:
            cnt+=1
        elif arr[i]== 0 :
                temp.append(cnt)
                cnt=0
    if arr[-1] == 1:
         temp.append(cnt)

    return max(temp)
arr=[1,1,1,1,0,1,1,1,1,1]
print(max_consecutive_one(arr))

