def find(number,finger):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                    '4': (1, 0), '5': (1, 1), '6': (1, 2),
                    '7': (2, 0), '8': (2, 1), '9': (2, 2),
                    '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    #전화번호 목록은 이미 정해져 있는 데이터고, 각 번호마다 좌표가 정해진걸로 볼수 있으니까
    # dic구조를 이용하면 거리 계산이 뭔가 가능할 것 같다                
    number=str(number)
    distance=abs(location[number][0]-location[finger][0])+abs(location[number][1]-location[finger][1])
    #거리 계산은 유클리드 거리와, 맨하튼 거리가 있다.
    # 유클리드는 그냥 피타고라스 정리 쓰는거고, 맨하튼은 x좌표 차이의 절대값+y좌표 차이 절대값이다.
    return distance
def solution(numbers, hand):
    answer = ''
    leftfinger='*'
    rightfinger='#'
    for number in numbers:
        if number in [1,4,7]:
            answer+='L'  
            leftfinger=str(number)
        elif number in [3,6,9]:
            answer+='R'
            rightfinger=str(number)
        else:
            #손가락에서 타켓 넘버까지의 거리 계산 너무 복잡할땐 
            # 함수화로 하나씩 해보자
            # 가운데 숫자 2580중에 하나를 누를때는 이전 손가락이 누르는 곳과 타켓 번호의
            # 거리를알아야한다! 이게 첫번째 생각
            # 거리만 알아내는 함수를 만들고 그다음걸 진행해야함
            leftdistance=find(number,leftfinger)
            rightdistance=find(number,rightfinger)
            if leftdistance<rightdistance:
                answer+='L'
                leftfinger=str(number)
            elif rightdistance<leftdistance:
                answer+='R'
                rightfinger=str(number)
            elif leftdistance==rightdistance:
                if hand == 'left':
                    answer+='L'
                    leftfinger=str(number)
                else:
                    answer+='R'
                    rightfinger=str(number)
            
            
    return answer