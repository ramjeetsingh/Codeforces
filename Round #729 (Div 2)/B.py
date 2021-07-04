import math

t = int(input())
for _ in range(0,t):
	n,a,b = input().split(" ")
	n = int(n)
	a = int(a)
	b = int(b)

	'''
	all methods are giving correct answer on test cases but TLE when submitted :(
	'''
	''' 
	METHOD 1

	if a == 1:
		n -= 1
		if (n/b)%1 == 0:
			print("Yes")
	else:
		sum_wala = (n-1)/b
		power_wala = math.log(n,a)
		if sum_wala%1 == 0:
			print("Yes")
		elif power_wala%1 == 0:
			print("Yes")
		else:
			current_no = n
			printed = False
			while current_no > 1:
				current_no_after_div = current_no/a
				if current_no_after_div%1 == 0:
					current_no = current_no_after_div
				else:
					current_no -= b
	
				if current_no == 1:
					print("Yes")
					printed = True
					break
	
			if printed == False:
				print("No")
	'''
	'''
	METHOD 2

	power = 0
	printed = False
	while n - a**power >= 0:
		if (n - a**power)%b == 0:
			print("Yes")
			printed = True
			break
		else:
			power += 1
	if printed == False:
		print("No")
	'''
	'''
	METHOD 3

	printed = False
	if a == 1:
		if ((n-1)/b)%1 == 0:
			print("Yes")
		else:
			print("No")
	else:
		for p in range(0,35):
			if a**p <= n:
				if ((n - (a**p))/b)%1 == 0:
					print("Yes")
					printed = True
					break
		if printed == False:
			print("No")
	'''