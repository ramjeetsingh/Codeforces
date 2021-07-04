w = int(input())
p1 = 0
p2 = 0
check = 0
for i in range(1,w):
	p1 = i
	p2 = w - p1
	if p1%2==0 and p2%2==0:
		check += 1

if check == 0:
	print("NO")
else:
	print("YES")