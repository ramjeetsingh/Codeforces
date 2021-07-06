t = int(input())
for _ in range(0,t):
	n,k = map(int,input().split(" "))
	
	if k == 1:
		if n%2 == 0:
			print("NO")
		else:
			print("YES")
	else:
		if k%2 == 0:
			if n%2 == 1:
				print("NO")
			else:
				if n >= k**2:
					print("YES")
				else:
					print("NO")
	
		else:
			if n%2 == 0:
				print("NO")
			else:
				if n >= k**2:
					print("YES")
				else:
					print("NO")			
