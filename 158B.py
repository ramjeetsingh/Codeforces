n = int(input())
no_per_grp = list(map(int,input().split(" ")))

grps_per_populn = {1:0, 2:0, 3:0, 4:0}
for i in range(0,len(no_per_grp)):
	grps_per_populn[no_per_grp[i]] += 1

cabs = grps_per_populn[4]

one_three_pairs = min(grps_per_populn[1], grps_per_populn[3])
cabs += one_three_pairs

one_remaining = 0
if grps_per_populn[3] > grps_per_populn[1]:
	cabs += (grps_per_populn[3] - grps_per_populn[1])
elif grps_per_populn[3] < grps_per_populn[1]:
	cabs += (grps_per_populn[1] - grps_per_populn[3])//4
	one_remaining = (grps_per_populn[1] - grps_per_populn[3])%4

two_pairs = grps_per_populn[2]//2
cabs += two_pairs
two_remaining = grps_per_populn[2]%2

if two_remaining == 0 and one_remaining != 0:
	cabs += 1
elif two_remaining == 1:
	cabs += 1
	if one_remaining > 2:
		cabs += 1

print(cabs)