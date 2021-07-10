# Giving WA.. IDK why.  :\

t = int(input())
for _ in range(0,t):
	space = input()
	k,n,m = map(int,input().split(" "))
	no_of_lines = k

	mono_oprns = list(map(int,input().split(" ")))
	poly_oprns = list(map(int,input().split(" ")))

	common_time_limit = min(n,m)

	printed = False
	ans = []
	for i in range(0,common_time_limit):
		m_oprn = mono_oprns[i]
		p_oprn = poly_oprns[i]

		if m_oprn == 0:
			ans.append(0)
			no_of_lines += 1
		if p_oprn == 0:
			ans.append(0)
			no_of_lines += 1

		if m_oprn != 0:
			if m_oprn > no_of_lines:
				print(-1)
				printed = True
				break
			else:
				ans.append(m_oprn)

		if printed == False:
			if p_oprn != 0:
				if p_oprn > no_of_lines:
					print(-1)
					printed = True
					break
				else:
					ans.append(p_oprn)


	if n>m and printed == False:
		for j in range(common_time_limit,n):
			m_oprn = mono_oprns[j]
			if m_oprn == 0:
				ans.append(0)
				no_of_lines += 1
			else:
				if m_oprn > no_of_lines:
					print(-1)
					printed = True
					break
				else:
					ans.append(m_oprn)

	if m>n and printed == False:
		for j in range(common_time_limit,m):
			p_oprn = poly_oprns[j]
			if p_oprn == 0:
				ans.append(0)
				no_of_lines += 1
			else:
				if p_oprn > no_of_lines:
					print(-1)
					printed = True
					break
				else:
					ans.append(p_oprn)

	if printed == False:
		for i in range(0,len(ans)):
			print(ans[i], end = " ")
		print()