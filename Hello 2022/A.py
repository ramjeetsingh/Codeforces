t = int(input())
for _ in range(0,t):
    n,k = map(int,input().split())

    if n == 1:
        print('R')

    elif k > (int(n//2) + n%2):
        print(-1)

    else:
        R_done = 0
        for line in range(1,n+1):
            if line%2 == 0 or R_done == k:
                print("."*n)
            else:
                print("."*(line-1) + "R" + "."*(n-line))
                R_done += 1
