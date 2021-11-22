t = int(input())
for _ in range(0,t):
	x, y = map(int,input().split(" "))

	distance = x + y
	valid_dist = int(distance//2)
	c = []
	c2 = []

	if distance % 2 == 1:
		print(-1,-1)

	else:
		a = 0
		b = valid_dist
		while a <= valid_dist:
			c.append([a,b])
			a += 1
			b -= 1

		for p in c:
			if (abs(x - p[0]) + abs(y - p[1])) == valid_dist:
				c2.append(p)

		if len(c2) == 0:
			print(-1,-1)
		else:
			print(c2[0][0], c2[0][1])