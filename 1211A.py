'''The problem was from Kotlin Heros but this python code works fine on all given and custom made test cases.'''

n = int(input())
comp = list(map(int,input().split(" ")))

prblm_per_comp = {}
for i in range(0,len(comp)):
	if comp[i] in prblm_per_comp.keys():
		prblm_per_comp[comp[i]].append(i+1)
	else:
		prblm_per_comp[comp[i]] = [i+1]

if len(prblm_per_comp) < 3:
	print(-1,-1,-1)
else:
	selected_comp = []
	for i in prblm_per_comp.keys():
		if len(selected_comp) == 3:
			break
		else:
			if len(selected_comp) == 0:
				selected_comp.append(i)
			elif len(selected_comp) == 1:
				if i > selected_comp[0]:
					selected_comp.append(i)
				else:
					selected_comp.insert(0,i)
			else:
				if i > selected_comp[1]:
					selected_comp.append(i)
				elif i < selected_comp[0]:
					selected_comp.insert(0,i)
				else:
					selected_comp.insert(1,i)

	for c in selected_comp:
		print(prblm_per_comp[c][0], end = " ")