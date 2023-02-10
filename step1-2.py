# 방울

# 10.0/100.0
# 정확성 테스트 10개 중 1개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(bell):
    answer = 0

    if 1 or 2 not in bell:  # 배열이 1이나 2로만 구성된 경우
        answer = 0

    if len(bell) % 2 == 0:
        max = len(bell)
    else:
        max = len(bell) - 1

    while max >= 2:
        for i in range(len(bell)):
            try:
                test = bell[i : i + max]

                if len(test) < max:
                    break

                if test.count(1) == test.count(2):
                    answer = max

                    return answer

            except IndexError:
                break

        max -= 2

    return answer