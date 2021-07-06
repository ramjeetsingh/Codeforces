t = int(input())
for _ in range(0,t):
	n = int(input())
	skills = list(map(int,input().split(" ")))

	people_per_skill = {}
	for i in range(0,len(skills)):
		if skills[i] in people_per_skill.keys():
			people_per_skill[skills[i]] += 1
		else:
			people_per_skill[skills[i]] = 1

	people_with_highest_skill = 0
	for i in people_per_skill.keys():
		if people_per_skill[i] > people_with_highest_skill:
			people_with_highest_skill = people_per_skill[i]

	len_team_1 = len(people_per_skill) - 1
	len_team_2 = people_with_highest_skill
	if len_team_1 == len_team_2:
		print(len_team_1)
	elif len_team_1 > len_team_2:
		print(len_team_2)
	else:
		diff = len_team_2 - len_team_1
		if diff <= 2:
			print(len_team_2 - 1)
		else:
			print(len_team_1 + 1)
