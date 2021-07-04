t = int(input())
for _ in range(0,t):
	n = int(input())
	if n%2 == 0:
		pairs = int(n/2)
		for i in range(1,pairs+1):
			print(2*i,end = " ")
			print(2*i - 1, end = " ")

	else:
		pairs = int(n//2) - 1
		for i in range(1,pairs+1):
			print(2*i,end = " ")
			print(2*i - 1, end = " ")

		print(n,n-2,n-1, end = " ")

	print()