n,m,a,b = map(int,input().split())

if m*a <= b:
    print(n*a)
else:
    print(n//m*b+n%m*a) if n%m*a <= b else print(n//m*b+b)