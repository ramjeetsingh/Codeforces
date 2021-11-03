def sum_of_digits(n):
	sum_dig= 0
	while n:
		sum_dig += n%10
		n //= 10

	return sum_dig
		

k = int(input())

no = 19

while k:
	if sum_of_digits(no) == 10:
		k -= 1

	no += 1

print(no - 1)