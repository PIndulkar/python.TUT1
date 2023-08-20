def insertionSort(l):
	n = len(l) 
	
	if n <= 1:
		return 

	for i in range(1, n): 
		key = l[i]
		j = i-1
		while j >= 0 and key < l[j]: 
			l[j+1] = l[j] 
			j -= 1
			print("j in while:",j)
		print("j in for:",j)	
		l[j+1] = key 


l = [12, 11, 13, 5, 6]
insertionSort(l)
print(l)
