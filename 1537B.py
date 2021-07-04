t = int(input())
for _ in range(0,t):
	n,m,i,j = map(int,input().split(" "))

	if (i==1 and j==1) or (i==1 and j==m):
		print(n,1,n,m)
	elif (i==n and j==m) or (i==n and j==1):
		print(1,1,1,m)
	else:
		print(1,1,n,m)