t = int(input())
for _ in range(0,t):
	empty = input()
	xa, ya = map(int,input().split(" "))
	xb, yb = map(int,input().split(" "))
	xf, yf = map(int,input().split(" "))

	ans = abs(xa - xb) + abs(ya - yb)
	if ((yf == ya) and (yf == yb)) and ((xf > min(xa,xb)) and (xf < max(xa,xb))):
		ans += 2
	elif ((xf == xa) and (xf == xb)) and ((yf > min(ya,yb)) and (yf < max(ya,yb))):
		ans += 2

	print(ans)