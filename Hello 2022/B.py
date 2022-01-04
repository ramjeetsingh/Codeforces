'''
gives correct answers but TLE
'''

t = int(input())
for _ in range(0,t):
    n = int(input())
    li = []
    ri = []
    ci = []

    for _ in range(1,n+1):
        l,r,c = map(int,input().split())
        li.append(l)
        ri.append(r)
        ci.append(c)

    l_set = 0
    r_set = 0
    c_set = 0
    r_set_on_ind = 0
    l_set_on_ind = 0
    c_set_on_ind = 0

    for s in range (1, n+1):
        if s == 1:
            print(ci[0])
            l_set = li[0]
            r_set = ri[0]
            c_set = ci[0]

        else:
            if ri[s-1] < r_set:
                print(c_set)

            elif ri[s-1] == r_set:
                if ci[s-1] < ci[c_set_on_ind]:
                    c_set -= ci[c_set_on_ind]
                    c_set += ci[s-1]
                    c_set_on_ind = s-1
                    print(c_set)

                else:
                    print(c_set)

            else:
                if li[s-1] <= l_set:
                    l_set = li[s-1]
                    r_set = ri[s-1]
                    c_set = ci[s-1]
                    l_set_on_ind = s-1
                    r_set_on_ind = s-1
                    c_set_on_ind = s-1

                else:
                    r_set = ri[s-1]
                    r_set_on_ind = s-1
                    c_set = ci[s-1] + ci[l_set_on_ind]
                    c_set_on_ind = s-1

                print(c_set)        

                

                    

                   
