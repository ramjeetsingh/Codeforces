def non_zero_present(l):
	ans = False
	for i in range(0,len(l)):
		if l[i] != 0:
			ans = True
			break

	return ans

n,m = map(int,input().split(" "))

cities_won = {}

for i in range(0,m):
	v = list(map(int,input().split(" ")))
	max_votes = 0
	max_votes_to = 0
	for j in range(0,len(v)):
		if v[j] > max_votes:
			max_votes = v[j]
			max_votes_to = j+1

	if_nonzero = non_zero_present(v)

	if if_nonzero == True:
		if max_votes_to in cities_won.keys():
			(cities_won[max_votes_to]).append(i+1)
		else:
			(cities_won[max_votes_to]) = [i+1]
	else:
		if 1 in cities_won.keys():
			(cities_won[1]).append(i+1)
		else:
			cities_won[1] = [i+1]

max_cities = 0
winner = 1

for k in range(1,n+1):
	if k in cities_won.keys():
		if len(cities_won[k]) > max_cities:
			winner = k
			max_cities = len(cities_won[k])

print(winner)