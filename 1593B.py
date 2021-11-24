def if_25(n):
	five_present = False
	no = str(n)
	five_at = 0

	for i in range(len(no)-1, 0, -1):
		if no[i] == '5':
			five_present = True
			five_at = i
			break

	if five_present == False:
		return (-1)
	else:
		two_present = False
		two_at = 0

		for i in range(five_at, -1, -1):
			if no[i] == '2':
				two_present = True
				two_at = i
				break

		if two_present == False:
			return (-1)
		else:
			return (((five_at - two_at) - 1) + ((len(no) - five_at)-1))

def if_50(n):
	zero_present = False
	no = str(n)
	zero_at = 0

	for i in range(len(no)-1, 0, -1):
		if no[i] == '0':
			zero_present = True
			zero_at = i
			break

	if zero_present == False:
		return (-1)
	else:
		five_present = False
		five_at = 0

		for i in range(zero_at, -1, -1):
			if no[i] == '5':
				five_present = True
				five_at = i
				break

		if five_present == False:
			return (-1)
		else:
			return (((zero_at - five_at) - 1) + ((len(no) - zero_at)-1))

def if_75(n):
	five_present = False
	no = str(n)
	five_at = 0

	for i in range(len(no)-1, 0, -1):
		if no[i] == '5':
			five_present = True
			five_at = i
			break

	if five_present == False:
		return (-1)
	else:
		seven_present = False
		seven_at = 0

		for i in range(five_at, -1, -1):
			if no[i] == '7':
				seven_present = True
				seven_at = i
				break

		if seven_present == False:
			return (-1)
		else:
			return (((five_at - seven_at) - 1) + ((len(no) - five_at)-1))

def if_100(n):
	first_0_present = False
	no = str(n)
	first_0_at = 0

	for i in range(len(no)-1, 0, -1):
		if no[i] == '0':
			first_0_present = True
			first_0_at = i
			break

	if first_0_present == False:
		return (-1)
	else:
		second_0_present = False
		second_0_at = 0

		for i in range(first_0_at-1, 0, -1):
			if no[i] == '0':
				second_0_present = True
				second_0_at = i
				break

		if second_0_present == False:
			return (-1)
		else:
			return (((first_0_at - second_0_at) - 1) + ((len(no) - first_0_at)-1))


t = int(input())
for _ in range(0,t):
	n = int(input())
	ans = [if_25(n),if_50(n),if_75(n),if_100(n)]
	possible_ans = []

	for i in range(0,len(ans)):
		if ans[i] != -1:
			possible_ans.append(ans[i])

	if len(possible_ans) == 0:
		print(-1)
	else:
		print(min(possible_ans))