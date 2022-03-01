t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if k > n:
        print("NO")
    else:
        if n%2 == 1:
            if k%2 == 0:
                print("NO")
            else:
                print("YES")
                ans = [1]*(k-1) + [n - k + 1]
                print(*ans)

        else:
            if k%2 == 0:
                print("YES")
                ans = [1]*(k-1) + [n - k + 1]
                print(*ans)
            else:
                ans = [2]*(k-1)
                rem = n - 2*(k-1)
                if rem <= 0 or rem%2 == 1:
                    print("NO")
                else:
                    print("YES")
                    ans += [rem]
                    print(*ans)               
