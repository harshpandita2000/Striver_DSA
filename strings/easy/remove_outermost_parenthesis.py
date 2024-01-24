def remove_ele(s):
    open = 0
    close = 0
    list = []
    start = 0
    for i in range(len(s)):
        if s[i] == "(" :
            open += 1
        elif s[i] == ")":
            close += 1
        if open == close:
            list.append(s[start+1:i])
            start = i+1
            open = 0
            close = 0
    return "".join(list)  

# s = "(()())(())"
s = "(()())(())(()(()))"
print(remove_ele(s))                #Input: s = "(()())(())"
                                    #Output: "()()()"
s= s.split(" ")
rever
   