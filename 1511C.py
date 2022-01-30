n, q = map(int, input().split())
colors = list(map(int, input().split()))
query = list(map(int, input().split()))

first_color = {}
for i in range(0,n):
    if colors[i] not in first_color.keys():
        first_color[colors[i]] = i
    
for i in range(0,q):
    if query[i] in first_color.keys():
        print(first_color[query[i]] + 1, end=" ")
    
    for j in first_color.keys():
        if first_color[j] < first_color[query[i]]:
            first_color[j] += 1
    
    first_color[query[i]] = 0