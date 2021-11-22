t = int(input())
for _ in range(0,t):
	n,a,b = map(int,input().split(" "))

	left_half = [a]
	right_half = [b]
	
	remaining = []
	for i in range(1,n+1):
		remaining.append(i)
	remaining.remove(a)
	remaining.remove(b)

	if b == int(n//2) and a < b:
		print(-1)
	elif b < int(n//2):
		print(-1)
	elif a > int(n//2)+1:
		print(-1)
	elif a == int(n//2)+1 and a < b:
		print(-1)
	else:
		for i in range(1,n+1):
			if i!=a and i!=b:
				if i < a and i != b:
					right_half.append(i)
					remaining.remove(i)
				elif i > b and i != a:
					left_half.append(i)
					remaining.remove(i)

		ans = left_half + remaining + right_half

		for i in ans:
			print(i, end=" ")
		print()