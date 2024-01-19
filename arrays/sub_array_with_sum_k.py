#2nd optimisation avoid using temp arr
def sum_k(arr, k):
    arr_sum = 0
    leng=0
    i = 0
    j = 0
    n = len(arr)                         
    while i < n:                   
        j = i
        arr_sum = 0
        while j < n:
            arr_sum += arr[j]
            if arr_sum == k:
                leng=max(leng, j - i + 1)
            j += 1
        i += 1
    print(leng)
    
#arr = [17, 0, 0, 0, 0, 17, 0, 0]
# arr = [17, 0, 0, 0, 0, 17, 0, 0, -1,1]
#arr=[3,-1,-2,-4,4,0]
arr=[0, 1 ,1, -1 , 0,-1]

sum_k(arr, 0)
#TC:O(N^2) #BECAUSE  inner loop efficiently traverses the array only once,while outer loop runs n times
#SC:O(1)








