from collections import deque
def solution(prices): #그냥 for문으로 푸는법
    answer = [0]*len(prices) #이 방법은 answer의 마지막 인덱스는 어차피 0이니까 체크 안해버림
    
    for i in range(len(prices)-1): #그래서 range가 len(prices)-1까지
        for j in range(i,len(prices)-1):
            if prices[i]<=prices[j]: #대신 이중for문에서 같은 i,j값이어도 확인
                answer[i]+=1
            else:
                break
    return answer

def solution(prices): #deque이용해서 푸는법
    answer = []
    
    que_prices = deque(prices)
    
    while que_prices :
        price = que_prices.popleft()
        up_time = 0
        for n in que_prices :
            up_time += 1 #같은 i,j인덱스를 확인을 못함 popleft하고 비교하니까 그래서 +1을 먼저해줌(같은 인덱스면 어차피 +1되니까==같은 시간내에서는 주가 안떨어지니까)
            if price > n :
                break
        answer.append(up_time)
        
    return answer    