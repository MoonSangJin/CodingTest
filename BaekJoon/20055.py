#구현
from collections import deque
n,k = map(int, input().split())
convey=deque(list(map(int,input().split())))
robot = deque([0] * n)
answer=1
while True:
    #1단계
    convey.rotate(1)
    robot.rotate(1)
    robot[-1]=0

    #2단계
    for i in range(n-2,-1,-1):
        if robot[i]==1 and robot[i+1]==0 and convey[i+1]>0:
            robot[i]=0
            robot[i+1]=1
            convey[i+1]-=1
    robot[-1]=0

    #3단계
    if robot[0]==0 and convey[0]>0:
        robot[0]=1
        convey[0]-=1
    
    #4단계
    if convey.count(0)>=k:
        break

    answer+=1
print(answer)