n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(input())
answer=[]
for i in range(n-7):
    for j in range(m-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if data[k][l]!='W': #W가 아니라 B면
                        first_W+=1      #W로 시작할때 다 바꿔줘야됨
                    if data[k][l]!='B': #B가 아니라 W면
                        first_B+=1      #B로 시작할때 다 바꿔줘야됨
                else:
                    if data[k][l]!='W': #W가 아니라 B면
                        first_B+=1      
                    if data[k][l]!='B':
                        first_W+=1
        answer.append(first_W)
        answer.append(first_B)
print(min(answer))                                        