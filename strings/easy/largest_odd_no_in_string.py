def maxlarge(s):  #123
    maxx=0
    for i in range(len(s)):
        if int(s[i])%2 !=0:
           maxx = max(maxx,int(s[i]))
    return maxx
        
s="123"
print(maxlarge(s))

