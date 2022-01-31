def no_of_diff_dig(a,b):
    a = str(a)
    b = str(b)

    if len(a) < len(b):
        a = "0"*(len(b)-len(a)) + a
    elif len(b) < len(a):
        b = "0"*(len(a) - len(b)) + b

    count = 0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            count += 1

    return count

t = int(input())
for _ in range(0,t):
    n = int(input())

    if n%7 == 0:
        print(n)
    else:
        lower_div = n - n%7
        upper_div = lower_div + 7

        diff_lower_dig = no_of_diff_dig(n, lower_div)
        diff_upper_dig = no_of_diff_dig(n, upper_div)

        if diff_lower_dig < diff_upper_dig:
            print(lower_div)
        elif diff_lower_dig > diff_upper_dig:
            print(upper_div)
        else:
            print(upper_div)