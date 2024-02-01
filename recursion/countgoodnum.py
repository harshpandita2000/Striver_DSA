class Solution(object):
    def countGoodNumbers(self, n):
        mod = 10**9 + 7
        def power_recursivee(x,n):
            if n < 0:
                n = -n
                x = 1/x
            if n == 0:
                return 1
            if n % 2 == 0:
                return  power_recursivee(x*x % mod,n//2)% mod
            else:
                return (x % mod* power_recursivee(x,n-1))%mod
        result = power_recursivee(5,(n+1)//2) * power_recursivee(4,n//2)%mod
        return result