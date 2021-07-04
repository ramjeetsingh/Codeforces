t = int(input())
for _ in range(0,t):
	n = int(input())
	bin_of_n = bin(n)
	bin_of_n = bin_of_n[2:len(bin(n))]
	no_of_zeroes = len(bin_of_n) - 1
	dec_of_boundary = 2**no_of_zeroes
	print(dec_of_boundary-1