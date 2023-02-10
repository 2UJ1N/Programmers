# 완주하지 못한 선수

# 58.3/100.0
# 정확성 테스트 7개 중 7개 통과
# 효율성 테스트 5개 중 0개 통과


def solution(participant, completion):
    answer = ''

    for i in participant:
        if i not in completion:
            answer = i
        else:
            completion.remove(i)  # 예제 3의 경우 고려
    return answer

'''
def solution(participant, completion):
    answer = ''
    
    for i in participant:

        if participant.count(i) != completion.count(i):
            answer = i
            return answer

        if i not in completion:
            answer = i
            return answer

    return answer
'''