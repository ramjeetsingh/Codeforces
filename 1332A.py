t = int(input())
for _ in range(0,t):
    a,b,c,d = map(int,input().split())
    x,y,x1,y1,x2,y2 = map(int,input().split())

    up_down = False
    left_rgt = False

    current = y
    moves_down = c
    moves_up = d

    if moves_up == 0 :
        if moves_down > abs(y1 - current) :
            up_down = False
        else:
            up_down = True
    else:
        current = min(y2, (current + moves_up))
        moves_up -= abs(y - current)
        if moves_up == 0:
            if moves_down > abs(y1 - current):
                up_down = False
            else:
                up_down = True
        else:
            new_current = current - moves_down + moves_up
            if y1 <= new_current <= y2:
                up_down = True
            else:
                up_down = False

    current = x
    moves_left = a
    moves_right = b

    if moves_right == 0:
        if moves_left > abs(x1 - current):
            left_rgt = False
        else:
            left_rgt = True
    else:
        current = min(x2, (current + moves_right))
        moves_right -= abs(x - current)
        if moves_right == 0:
            if moves_left > abs(x1 - current):
                left_rgt = False
            else:
                left_rgt = True
        else:
            new_current = current - moves_left + moves_right
            if x1 <= new_current <= x2:
                left_rgt = True
            else:
                left_rgt = False

    if (x1 == x2 and (a!=0 or b!=0)) or (y1 == y2 and (c!=0 or d!=0)):
        print("No")
    else:
        if up_down and left_rgt:
            print("Yes")
        else:
            print("No")