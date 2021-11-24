t = int(input())
for _ in range(0,t):
	s = input()

	no_of_0 = 0
	no_of_1 = 0

	for i in range(0,len(s)):
		if s[i] == '0':
			no_of_0 += 1
		else:
			no_of_1 += 1

	if no_of_1 == 0 or no_of_0 == 0:
		print(s)
	else:
		no_of_01 = 0
		no_of_10 = 0

		for i in range(0,len(s)-1):
			if s[i:i+2] == '01':
				no_of_01 += 1
			elif s[i:i+2] == '10':
				no_of_10 += 1

		if no_of_10 >= no_of_01:
			print('10'*len(s))
		else:
			print('01'*len(s))