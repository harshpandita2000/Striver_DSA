def fact(x):
    res = 1
    for i in range(1,x+1):
        res = res*i
    return res
x =5
print(fact(x))

# fact(5)= 5*fact(4)=5*4*fact(3)=5*4*3*fact(2)=5*4*3*2*fact(1)=5*4*3*2*1

def fact_recursive(x):
    if x == 1:
        return 1
    else:
        return x * fact_recursive(x-1)

x = 4
result = fact_recursive(4)

                                    
                                                  
    
