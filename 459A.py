x1, y1, x2, y2 = map(int, input().split())
if x1 == x2 or y1 == y2:
    if x1 == x2:
        sides = abs(y1 - y2)
        print(x1+sides, y1, x2+sides, y2)
    else:
        sides = abs(x1 - x2)
        print(x1, y1+sides, x2, y2+sides)
else:
    if abs(x1 - x2) == abs(y1 - y2):
        print(x1, y2, x2, y1)
    else:
        print(-1)