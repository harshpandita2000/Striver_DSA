
def missing_number(arr):
   for i in range(0,len(arr)+1):
      if arr[i]!= i + 1: 
        return i + 1
arr=[1,3]
print(missing_number(arr))

      