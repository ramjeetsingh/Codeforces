n, m = map(int, input().split())
prices = list(map(int, input().split()))

no_of_fruits = {}

for i in range(0,m):
    fruit = input()
    if fruit in no_of_fruits.keys():
        no_of_fruits[fruit] += 1
    else:
        no_of_fruits[fruit] = 1

fruits_no = list(no_of_fruits.values())

fruits_no.sort()
fruits_no.reverse()

prices_for_max = prices
prices_for_min = prices

prices_for_max.sort()
prices_for_min.sort()
prices_for_max.reverse()

max_price = 0
min_price = 0

for i in range(0,len(fruits_no)):
    max_price += fruits_no[i]*prices_for_max[i]
    min_price += fruits_no[i]*prices_for_min[n-i-1]

print(min_price, max_price)