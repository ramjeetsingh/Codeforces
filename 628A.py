import math

def highest_power_of_two(n):
	log = math.log(n,2)
	log = log//1
	return int(log)


n,b,p = map(int,input().split(" "))

remaining_praticipants = n
bottles = 0
towels = n*p
bottles_for_each_match = 2*b + 1

while remaining_praticipants > 1:
	k = highest_power_of_two(remaining_praticipants)
	playing_this_round = 2**k
	matches_in_this_round = int(playing_this_round//2)
	bottles += matches_in_this_round*((2*b) + 1)
	remaining_praticipants -= int(playing_this_round//2)

print(bottles,towels)

