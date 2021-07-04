t = int(input())
for _ in range(0,t):
	n = int(input())
	nos = list(map(int,input().split(" ")))

	even = []
	odd = []
	for i in range(0,len(nos)):
		if nos[i]%2 == 0:
			even.append(nos[i])
		else:
			odd.append(nos[i])

	if len(even) == len(odd):
		print("Yes")
	else:
		print("No")