t = int(input())
for _ in range(0,t):
	n = int(input())
	no = n//3
	n = n%3

	no_of_1 = no
	no_of_2 = no

	if n == 1:
		no_of_1 += 1
	elif n == 2:
		no_of_2 += 1

	print(no_of_1, no_of_2)