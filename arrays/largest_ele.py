def find_largest_element(arr):
    largest=arr[0]
    for ele in arr:
        if ele > largest:
            largest=ele
    print(largest)
    return largest

find_largest_element([1,3,4,22,11]) 
# print(largest_no)





