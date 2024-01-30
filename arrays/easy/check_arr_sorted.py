def check_arr_sorted(arr):
    ascend = True
    descend = True
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            ascend=False
        else:
            if arr[i]<arr[i+1]:
                descend=False
    return ascend or descend

array= [4,4,4]

check_arr_sorted(array)

# TC:O(N) #SInce we are traversing till size of n-1 but we ignore constant so its taking O(n)complexity..
# SC:O(1) as we created 3 variables and its a fixed size array ,so its taking O(1) space complexity..
# 1,2,3
# ele        ascend      descend
#           true           true
# 1         false           true
# 2         TRUE            false      
# true
#
# 
             

    

