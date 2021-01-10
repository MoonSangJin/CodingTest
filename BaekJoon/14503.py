#구현 로봇청소기

n,m=map(int,input().split())

d=[[0]*m for _ in range(n)] #컴프리헨션 이용하여 2차원 리스트 선언 및 초기화 d는 청소한 위치 저장하기위한 리스트

x,y,direction=map(int,input().split())

d[x][y]=1 #현재 좌표는 청소했다를 의미한다.

array=[]
for _ in range(n):
  array.append(list(map(int,input().split())))


dx=[-1,0,1,0] #방향에 따른 x값 변화
dy=[0,1,0,-1] #방향에 따른 y값 변화

def turn_left(): #turn_left시 방향 변화
  global direction
  direction-=1
  if direction==-1:
    direction=3


count=1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction] #회전하고 갈 위치 알아보기

  if d[nx][ny]==0 and array[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time=0
    continue
  else:
    turn_time+=1 #회전했는데 다 가봤거나 바다인 경우

  if turn_time==4:#사방이 다 못가는 곳인 경우
    nx=x-dx[direction]
    ny=y-dy[direction]

    #뒤로갈 위치가 갈 수 있으면 가기
    if array[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0  

print(count)    