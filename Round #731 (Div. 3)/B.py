t = int(input())
for _ in range(0,t):
	s = input()
	n = len(s)

	printed = False

	a_index = 0
	for i in range(0,len(s)):
		if s[i] == "a":
			a_index = i
			break

	all_orders = []
	for i in range(0,len(s)):
		all_orders.append(ord(s[i]))

	prev_no = 0
	next_no = 0
	if a_index == 0:
		a_reached = True
	else:
		a_reached = False

	for i in range(1,len(all_orders)):
		prev_no = all_orders[i-1]
		next_no = all_orders[i]

		if i-1 == a_index:
			a_reached = True

		if a_reached == False:
			if prev_no <= next_no:
				print("NO")
				printed = True
				break
		else:
			if prev_no >= next_no:
				print("NO")
				printed = True
				break


	if printed == False:
		max_ord = 97 + n - 1
		ordrs = []
	
		for i in range(0,len(s)):
			o = ord(s[i])
	
			if (o in ordrs) or (o > max_ord):
				print("NO")
				printed = True
				break

			ordrs.append(o)

	if printed == False:
		print("YES")
