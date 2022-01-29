n = int(input())
smallest_l = 0
largest_r = 0
segments = []

for i in range(0,n):
    l, r = map(int, input().split())
    segments.append([l,r,i+1])
    if i == 0:
        smallest_l = l
        largest_r = r
    else:
        if l < smallest_l:
            smallest_l = l
        if r > largest_r:
            largest_r = r

smallest_ones = []
for i in range(0,len(segments)):
    if segments[i][0] == smallest_l:
        smallest_ones.append(segments[i])

printed = False
for i in range(0,len(smallest_ones)):
    if smallest_ones[i][1] == largest_r:
        print(smallest_ones[i][2])
        printed = True
        break
        
if printed == False:
    print(-1)