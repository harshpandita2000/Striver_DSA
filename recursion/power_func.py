# 2^6 = (2*2)^3 = 4^3 = 64
# 4^3 = 4 *4^2 = 4*16 = 64
# 4^2 = (4*4)^1= 16^1 =16
# 16^1 = 16* 16^0= 16

def power_recursivee(x,n):
    if n < 0:
        n = -n
        x = 1/x
    if n == 0:
        return 1
    if n % 2 == 0:
        return  power_recursivee(x*x,n//2)
    else:
        return x * power_recursivee(x,n-1)                     

x = 2
n = -4
result = power_recursivee(x,n)                         
print(result)
              
def power(x,n):
    if n < 0:
        nn = -n
        x = 1/x
    else:
        nn = n
    ans = 1
    while nn:
        if nn % 2 == 0:
            x *= x
            nn //= 2
        else:
            ans = ans * x                                
            nn -= 1                                               
    return ans                                     

# res = power_recursive(x,n)
# print(res)
 ################################################################################### 
# #   x   nn  ans
#     2   6   1
#     4   3   1
#         2   4
#     16  1   4
#     16  0   64