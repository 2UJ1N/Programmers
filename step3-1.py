'''
def solution(participant, completion):
    d = {}

    for x in participant:
        d[x] = d.get(x, 0) + 1

    for x in completion:
        d[x] -= 1

    dnf = [k for k, v in d.items() if v != 0]
    answer = dnf[0]
    return answer
'''

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