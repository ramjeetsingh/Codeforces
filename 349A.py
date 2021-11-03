n = int(input())
people = list(map(int,input().split(" ")))

change = {25:0, 50:0, 100:0}

printed = False

for i in range(0,len(people)):
	if people[i] == 25:
		change[25] += 1

	elif people[i] == 50:
		change[50] += 1

		if change[25] == 0:
			print("NO")
			printed = True
			break
		else:
			change[25] -= 1

	else:
		change[100] += 1

		if change[25] >= 1 and change[50] >= 1:
			change[25] -= 1
			change[50] -= 1	

		elif change[25] >= 3:
			change[25] -= 3

		else:
			print("NO")
			printed = True
			break

if printed == False:
	print("YES")
	