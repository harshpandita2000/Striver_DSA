def get_single_element(arr):
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr
arr=[1,2,1,3,3]
print(get_single_element(arr))

# Property 1---XOR of two same numbers is always 0 i.e. a ^ a = 0.
# Property 2---XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a. 
# XOR is also  commutative and associative.