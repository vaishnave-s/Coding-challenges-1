def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			print(i,j)
      
			if A[j] > A[j+1]:

				A[j], A[j+1] = A[j+1], A[j]
				print("swap")

        

			else:
				print("no swap")

				break


B=[1,3,2,5,4]
insertion_sort1(B)
print(B)


