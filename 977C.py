n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

a.sort()

probable = a[k-1]

occ = 0
first_occ = -1
for i in range(0,len(a)):
    if a[i] == probable:
        if first_occ == -1:
            first_occ = i
        occ += 1
last_occ = first_occ + occ - 1

if n == k:
    print(a[-1])
elif k == 0:
    if a[0] == 1:
        print(-1)
    else:
        print(a[0]-1)
else:
    if occ == 1:
        print(probable)
    else:
        if k-1 == last_occ:
            print(probable)
        else:
            print(-1)