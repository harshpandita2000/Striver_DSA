
def missing_number_for_sorted(arr):
   for i in range(0,len(arr)): # 1 3 4 5
      if arr[i]!= i + 1: 
        return i + 1
      
arr=[1,11]
print(missing_number_for_sorted(arr))

def missing_number(arr):
   n = max(arr)
   a = sum(arr)
   s = (n*(n+1))//2
   return s - a
arr=[1,3,4]
print(missing_number(arr))



      