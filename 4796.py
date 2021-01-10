#그리디
#예외를 생각하자
i = 1
while 1:
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    a = V//P
    b = V%P
    if b>=L :
        print("Case " + str(i) + ": " + str(a*L + L))
    else:
        print("Case " +  str(i) + ": " + str(a*L+b))
    i += 1