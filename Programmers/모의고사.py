def solution(answers):
    count1 = count2 = count3 = 0  # 0으로 초기화
    a = [1, 2, 3, 4, 5]  # 각 학생들의 찍는 패턴
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []

    for i in range(len(answers)):  # 인덱스 0부터 인덱스 len(answers)-1까지 반복
        if(answers[i] == a[i % len(a)]):
            count1 += 1
        if(answers[i] == b[i % len(b)]):
            count2 += 1
        if(answers[i] == c[i % len(c)]):
            count3 += 1  # 여기까지하면 count1,count2,count3에 각각의 정답 갯수가 담긴다 이걸 어떻게 비교할까
    answer_temp = [count1, count2, count3]
    # enumberate함수를 사용하면 인덱스랑 인덱스의 값을 튜플() 로 반환한다.
    for index, value in enumerate(answer_temp):
        if(value == max(answer_temp)):  # 그런데 for문 돌면서 value가 각 인덱스의 값이 될텐데 max값과 같은거면 그 인덱스가 가장 많이 맞힌사람
            # 그냥 index+1(시작이 0이니까)을 return 하지 않고 append를 쓴이유는 같은 개수를 맞힌 사람이 여러명이 있을 수도 있다.
            result.append(index+1)
    return result  # 그걸 오름차순으로 return하라고 했는데 sort를 써야되나 했는데 어차피 인덱스를 return하는 것이고, for문은 어차피 인덱스 0부터 시작이니까
    # 그냥 append하면 자동으로 인덱스 오름차순 형태로 들어간다.
