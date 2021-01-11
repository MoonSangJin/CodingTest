# 해시
import collections
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = ''
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    result = list(a-b)
    answer = result[0]

    return answer
# collections에 내장된 함수인 Counter()는 Dic과 같이 hash형 자료들의 값의 개수를 셀 때 사용
# Counter({'mislav': 2, 'ana': 1, 'stanko': 1}) 식으로 나옴
# Dic처럼 {key:value} 형식으로 만들어짐
# Counter() 객체끼리 빼는 것도 가능, a-b 의 결과가 Counter({'mislav': 1})이 나왔다. 이걸 list로 바꿔서 0번째 원소만 가져오면됨


# def solution(participant, completion):  유효성 통과 못함 O(n^2)인듯하다.
#     answer = ''
#     for i in participant:
#         if i in completion:
#             completion.remove(i)
#         else:
#             answer = i

#     return answer
