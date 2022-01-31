t = int(input())
for _ in range(0,t):
    s = input()

    no_of_0 = 0
    no_of_1 = 0

    for i in range(0,len(s)):
        if s[i] == '0':
            no_of_0 += 1
        else:
            no_of_1 += 1

    if no_of_0 != no_of_1:
        print(min(no_of_0,no_of_1))
    else:
        print(no_of_0 - 1)