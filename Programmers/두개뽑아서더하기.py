numbers = [2, 1, 3, 4, 1]
result = [2, 3, 4, 5, 6, 7]


def solution(numbers):
    answer = []
    for i in range(len(numbers)):  # len(numbers)는 5, index 0부터 numbers의 길이-1까지 반복, 여기서는 0~4
        for j in range(i+1, len(numbers)):  # 유사한 방식으로 이중 포문 돌리면 두개 뽑는 모든 경우 탐색가능
            # i랑 j는 인덱스에 불과하니까 두 수의 합을 구하려면 numbers[i]같은 방식으로 더해서 answer에 없을때만 추가한다. 이를 통해 중복제거
            if (numbers[i]+numbers[j]) not in answer:
                # answer는 list형식이고 list에 추가할 때는 append 메소드를 사용한다.
                answer.append(numbers[i]+numbers[j])
    return sorted(answer)  # 오름차순으로 담으래서 sorted함수 사용한다.
