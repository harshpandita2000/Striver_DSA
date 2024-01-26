# *********
#  *******
#   *****
#    ***
#     *

n= 5
for i in range(n):
    for space in range(i):
        print(' ',end='')
    for j in range(2*n-2*i-1):
        print('*',end='')
    for spacee in range(i):
            print(' ',end='')
    print()