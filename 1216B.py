n = int(input())
a = list(map(int,input().split(" ")))
temp = a
temp2 = []
order = {}
for i in range(0,len(a)):
	order[i+1] = a[i]

for i in range(0,len(order)):
	temp2.append(order[i+1]) 

cans = {}
for i in range(0,len(temp)):
	if temp[i] not in cans.keys():
		cans[temp[i]] = [i+1]
	else:
		cans[temp[i]] += [i+1]

a.sort()
a_all_diff = []
for i in range(0,len(a)):
	if a[i] not in a_all_diff:
		a_all_diff.append(a[i])

ans_ord = []
for i in range(0,len(a_all_diff)):
	ans_ord += cans[a_all_diff[i]]
ans_ord.reverse()

ans = 0
for i in range(0,len(ans_ord)):
	ans += i*temp2[ans_ord[i]-1] + 1

print(ans)
for i in range(0,len(ans_ord)):
	print(ans_ord[i], end=" ")