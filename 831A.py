n = int(input())
a = list(map(int, input().split()))

if n==1 or n==2:
    print("YES")

elif n==3:
    if a[0] == a[1]:
        if a[1] < a[2]:
            print("NO")
        else:
            print("YES")
    elif a[0] < a[1]:
        print("YES")
    else:
        if a[1] > a[2]:
            print("YES")
        else:
            print("NO")

else:
    if a[0] > a[1]:
        printed = False
        for i in range(1, len(a)-1):
            if a[i] <= a[i+1]:
                print("NO")
                printed = True
                break
        if printed == False:
            print("YES")
    
    elif a[0] == a[1]:
        still_eq = True
        printed = False
        for i in range(1, len(a)-1):
            if still_eq == True:
                if a[i] == a[i+1]:
                    continue
                elif a[i] < a[i+1]:
                    print("NO")
                    still_eq = False
                    printed = True
                    break
                else:
                    still_eq = False

            else:
                if a[i] <= a[i+1]:
                    print("NO")
                    printed = True
                    break
                else:
                    continue
        if printed == False:
            print("YES")

    else:
        still_inc = True
        equal = False
        printed = False
        for i in range(1, len(a)-1):
            if still_inc == True:
                if a[i] < a[i+1]:
                    continue
                elif a[i] == a[i+1]:
                    still_inc = False
                    equal = True
                else:
                    still_inc = False
            else:
                if equal == True:
                    if a[i] == a[i+1]:
                        continue
                    elif a[i] < a[i+1]:
                        print("NO")
                        printed = True
                        break
                    else:
                        equal = False
                else:
                    if a[i] <= a[i+1]:
                        print("NO")
                        printed = True
                        break
                    else:
                        continue

        if printed == False:
            print("YES")