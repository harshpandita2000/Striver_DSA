#FIRST LEVEL OPTIMISATION JUST USED TEMP ARR AND A length variable that resulted in space reduction.
def sum_k(arr, k):
    temp=[]
    leng=0
    i = 0
    j = 0
    n = len(arr)
    while i < n:
        j = i
        temp = []
        while j < n:
            temp.append(arr[j])
            if sum(temp) == k:
               # sub_arr.append(temp)
                leng = max(leng,len(temp))
                break
            if sum(temp) < k:
                j += 1
            elif sum(temp) > k:
                break
        if i == n:
            break
        i += 1
    print(leng)

# arr = [2,3,4,4,1,8,9,2,4,3,1,1,1,1,1,4]
arr = [8,15,17,0,11 ]
sum_k(arr,17)
#TC:O(N^2)#because there are nested loops where the outer loop runs 'n' times, and the inner loop runs at most 'n' times in the worst case
#SC:O(N) # because of the temporary list temp which can grow up to the size of the input array.


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
               # sub_arr.append(temp)
                leng=max(leng, j - i + 1)
                break
            if arr_sum < k:
                j += 1
            elif arr_sum > k:
                break
        # if i == n:
        #     break
        i += 1
    print(leng)
    

# arr = [2,3,4,4,1,8,9,2,4,3,1,1,1,1,1,4]
# arr = [1,1,1,4,1,1,9,0,1,3,1,1,1,1,1]
# arr = [2,3,4,1,1]
    
arr = [8,15,17,0,11 ]
sum_k(arr, 17)
#TC:O(N) #BECAUSE  inner loop efficiently traverses the array only once,while outer loop runs n times
#SC:O(1)

#no error
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
                leng = max(leng, j - i + 1)
            j += 1
        i += 1
    print(leng)

arr = [17, 0, 0, 0, 0, 17, 0, 0]
sum_k(arr, 17)

#sliding wind approach
def sum_k_optimized(arr, k):
    n = len(arr)
    arr_sum = 0
    start = 0
    leng = 0

    for end in range(n):
        arr_sum += arr[end]

        while arr_sum > k:
            arr_sum -= arr[start]
            start += 1

        if arr_sum == k:
            leng = max(leng, end - start + 1)

    return leng
arr=[8, 15, 17, 0, 11]
print(sum_k_optimized(arr, 17))
# Iteration	 start	   end	   arr_      sumleng
# 1	          0	        0	    8	        0
# 2	          0	        1	    23	        2
# 3	          2	        2	    17	        2
# 4	          3	        3	    17	        2
# 5	          4	        4	    28	        2

