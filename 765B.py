s = input()
max_ascii = 0
done = []

for i in range(len(s)):
    if s[i] not in done:
        if s[i] != "a" and (ord(s[i])-1) not in done:
            print("NO")
            exit()
        else:
            if ord(s[i]) < max_ascii:
                print("NO")
                exit()
            else:
                max_ascii = ord(s[i])
                done.append(s[i])
                done.append(ord(s[i]))

print("YES")
