def union_sorted(arr1, arr2): 
	m, n = len(arr1), len(arr2) 
	i, j = 0, 0
	result = [] 
	while i < m and j < n: 
		if arr1[i] < arr2[j]: 
			result.append(arr1[i]) 
			i += 1
		elif arr2[j] < arr1[i]: 
			result.append(arr2[j]) 
			j += 1
		else: 
			result.append(arr1[i]) 
			i += 1
			j += 1
	result.extend(arr1[i:] + arr2[j:]) 
	return result 

arr1 = [1, 2, 3, 4,6] 
arr2 = [2, 3, 4, 5] 
result=union_sorted(arr1,arr2)
print(result)