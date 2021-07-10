t = int(input())
for _ in range(0,t):
	n = int(input())
	arr = list(map(int,input().split(" ")))

	odd = []
	even = []

	for i in range(0,len(arr)):
		if arr[i]%2 == 0:
			even.append(arr[i])
		else:
			odd.append(arr[i])

	if len(odd)%2 == 0:
		print("YES")
	else:
		inter_paired = False
		for j in range(0,len(odd)):
			if ((odd[j] + 1) in even) or ((odd[j] - 1) in even):
				inter_paired = True
				print("YES")
				break

		if inter_paired == False:
			print("NO")