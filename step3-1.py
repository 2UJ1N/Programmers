# 완주하지 못한 선수

# 100.0/100.0
# 정확성 테스트 7개 중 7개 통과 58.3
# 효율성 테스트 5개 중 5개 통과 41.7

def solution(participant, completion):
    # 딕셔너리 생성
    d = {}

    for i in participant:
        d[i] = d.get(i, 0) + 1

    for i in completion:
        d[i] -= 1

    for key, value in d.items():
        if value == 1:
            answer = key

    return answer