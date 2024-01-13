def check_arr_sorted(arr):
    ascend = True
    descend = True
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            ascend=False
        else:
            if arr[i]<arr[i+1]:
                descend=False
    print(ascend,descend)
    print(ascend or descend)
# array =[ 1,3,4,5]
# array= [5,4,3,2,1]
#array = [1,2,4,4,9]

array= [4,4,4]

check_arr_sorted(array)


# 1,2,3
# ele        ascend      descend
#           true           true
# 1         false           true
# 2         TRUE            false      
# true
#
# 
             

    

