t = int(input())
for _ in range(0,t):
	a = int(input())

	sides = 360/(180 - a)

	if sides == int(sides):
		print("YES")
	else:
		print("NO")