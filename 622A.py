n = int(input())

sum_just_before = 0
k = 1

while True:
	if sum_just_before < n:
		sum_just_before += k
		k += 1
	elif sum_just_before == n:
		break
	else:
		sum_just_before -= (k-1)
		break

diff = abs(n - sum_just_before)

if sum_just_before == n:
	print(k-1)
else:
	print(diff)