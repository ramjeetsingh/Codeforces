n,k = map(int, input().split(" "))
heights = list(map(int, input().split(" ")))

sum_of_hts = {0:0}
addn = 0
for i in range(0,len(heights)):
	addn += heights[i]
	sum_of_hts[i+1] = addn

min_ht = sum_of_hts[n]
ans = 0
for j in range(k,n+1):
	this_sum = sum_of_hts[j] - sum_of_hts[j-k]
	if this_sum <= min_ht:
		min_ht = this_sum
		ans = j -k +1

print(ans)