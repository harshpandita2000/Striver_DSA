def find_second_largest(arr):
    largest=arr[0]
    second_largest=arr[0]
    for ele in arr:
        if ele > largest:
            second_largest=largest
            largest =ele
        else:
            if ele >second_largest:
                second_largest=ele
    print(second_largest)

find_second_largest([1,8,10,20,30,25])