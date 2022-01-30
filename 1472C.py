t = int(input())
for _ in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))

    scores = {}
    for i in range(n-1,-1,-1):
        if i + a[i] >= n:
            scores[i] = a[i]
        else:
            scores[i] = a[i] + scores[i+a[i]]

    print(max(scores.values()))
    