n = int(input())

ans = 0
candies_left = n

i = 1

while candies_left > 0:
	candies_left -= i
	i += 1
	ans += 1

extra = abs(candies_left)

if ans == 1:
	print(1)
elif extra == 0:
	print(ans)
else:
	print(ans - 1)

for j in range(1,i):
	if j != extra:
		print(j, end = " ")