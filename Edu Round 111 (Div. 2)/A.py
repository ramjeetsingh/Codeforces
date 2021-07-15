t = int(input())
for _ in range(0,t):
	s = int(input())

	arr = [1]
	current_sum = 1
	diff_in_sum = s - current_sum
	current_len = 1

	while diff_in_sum > 0:
		if diff_in_sum >= ((2*current_len)+1):
			arr.append((2*current_len)+1)
			diff_in_sum -= ((2*current_len)+1)
			current_len += 1
		else:
			arr.append(diff_in_sum)
			diff_in_sum = 0

	print(len(arr))




	'''
	sum_remaining = s - 1
	arr = [1]
	current_no = 1

	while sum_remaining > 0:
		current_no += 2
		arr.append(current_no)
		sum_remaining -= current_no

	current_sum = sum(arr)
	extra = current_sum - s

	while extra > 0:
		if extra >= arr[-1]:
			extra -= arr[-1]
			arr = arr[0:len(arr)]
		else:
	'''
