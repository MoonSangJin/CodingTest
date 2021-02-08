#스택큐
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge=[0]*bridge_length #가상의 다리를 만들자
    
    while len(bridge)!=0:
        time+=1 #시간이 1초가면
        bridge.pop(0) #다리를 한칸 건너는거로 생각
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight: #다리위 트럭들 + 더 올릴수 있는지 체크
                bridge.append(truck_weights.pop(0))#더 올릴수 있으면 올려
            else:
                bridge.append(0) #더 못올리는경우
    return time