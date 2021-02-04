board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    bucket=[]
    
    for move in moves: #move가 세로열이 되는데
        for i in range(len(board)): #세로열 고정된 상태로 수직으로 내려가야됨
            if board[i][move-1]>0: #0보다 크면 인형이 있느 상태
                bucket.append(board[i][move-1]) #bucket 리스트에 추가해주고
                board[i][move-1]=0 #다시 비워둔다
                if len(bucket)>=2: #버킷에 최소 2개 이상은 있어야 서로 지워질 수 있고
                    if bucket[-1]==bucket[-2]: #맨 마지막꺼랑 맨 마지막에서 두번째꺼가 같으면 사라질것
                        answer+=2 #사라질때는 짝으로 사라지니까 인형갯수는 2개씩 증가
                        bucket.pop()
                        bucket.pop()
                        break   #사라졌으면 다음 move를 실행 위해 break
                break           #버킷에 2개 이하로 있으면 다음 인형을 버킷에 일단 넣어야되므로 다음 move 실행위해 break             
    return answer

print(solution(board,moves))
