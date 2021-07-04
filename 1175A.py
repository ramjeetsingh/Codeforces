  
t = int(input())
for _ in range(0,t):
	n,k = map(int,input().split(" "))
	ans = n%k
	if n >= k:
		n = n - n%k
		while n>1:
			if n%k == 0:
				n = n//k
				ans += 1
			else:
				ans += n%k
				n -= n%k
		if n != 0: 
			ans += 1
	print(ans)