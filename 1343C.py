t = int(input())
for _ in range(0,t):
    n = int(input())
    a = list(map(int, input().split(" ")))

    done_till = -1
    i = 0

    s = 0

    while done_till < n-1:
        i_at_start = i
        while i < n-1:
            if a[i]//abs(a[i]) == a[i+1]//abs(a[i+1]):
                i += 1
            else:
                break
        
        new_a = a[i_at_start:i+1]

        s += max(new_a)

        done_till = i
        i += 1
    
    print(s)
        