n,m = map(int,input().split(" "))
orig_size =  []
comp_size = []

for i in range(0,n):
	a,b = map(int,input().split(" "))
	orig_size.append(a)
	comp_size.append(b)

diff_in_size = []
for i in range(0,len(orig_size)):
	diff_in_size.append(orig_size[i] - comp_size[i])

diff_in_size.sort()
total_size = sum(orig_size)
ans = 0
ind = -1
printed = False

while ans <= n:
	if total_size <= m:
		print(ans)
		printed = True
		break
	else:
		total_size -= diff_in_size[ind+1]
		ans += 1
		ind -= 1

if printed == False:
	print(-1)