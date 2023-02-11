# 가장 큰 수

# 26.7/100.0
# 정확성 테스트 15개 중 4개 통과
# 효율성 테스트 5개 중 0개 통과

# 코드는 좋은데 시간초과로 11개 통과 못함

import itertools

def solution(numbers):
    word = list(map(str, numbers))
    all = []
    result = []

    tmp = itertools.permutations(word)
    all += tmp

    for i in all:
        string = ''
        for j in range(len(numbers)):
            string += i[j]
        result.append(int(string))

    answer = str(max(result))

    return answer

solution([3, 30, 34, 5, 9])