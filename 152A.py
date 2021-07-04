
n,m = map(int,input().split(" "))

topper_per_sub = {}
marks_per_student = {}

for i in range(1,n+1):
	a = input()
	marks_per_student[i] = a

	for j in range(0,len(a)):
		marks_in_this_sub = int(a[j])
		if j+1 not in topper_per_sub.keys():
			topper_per_sub[j+1] = [i]
		else:
			if marks_in_this_sub > int(marks_per_student[topper_per_sub[j+1][0]][j]):
				topper_per_sub[j+1] = [i]
			elif marks_in_this_sub == int(marks_per_student[topper_per_sub[j+1][0]][j]):
				topper_per_sub[j+1] += [i]

all_toppers = []
for i in topper_per_sub.values():
	all_toppers += i

all_diff_toppers = []
for i in range(0,len(all_toppers)):
	if all_toppers[i] not in all_diff_toppers:
		all_diff_toppers.append(all_toppers[i])

print(len(all_diff_toppers))