# 식사하는 철학자들

# 30.8/100.0
# 정확성 테스트 13개 중 4개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(satisfy, k):

    first = satisfy.index(max(satisfy))
    answer = 0

    # 만족도 최대인 사람이 먹을 때
    answer += max(satisfy)

    if first == len(satisfy) - 1:
        satisfy[0] = 0
        satisfy[first] = 0
        satisfy[first - 1] = 0
    elif first == 0:
        satisfy[len(satisfy) - 1] = 0
        satisfy[first] = 0
        satisfy[first + 1] = 0
    else:
        satisfy[first - 1] = 0
        satisfy[first] = 0
        satisfy[first + 1] = 0

    k -= 1

    while k > 0:
        next = satisfy.index(max(satisfy))
        answer += max(satisfy)
        k -= 1

        if next == len(satisfy) - 1:
            satisfy[0] = 0
            satisfy[next] = 0
            satisfy[next - 1] = 0
        elif next == 0:
            satisfy[len(satisfy) - 1] = 0
            satisfy[next] = 0
            satisfy[next + 1] = 0
        else:
            satisfy[next - 1] = 0
            satisfy[next] = 0
            satisfy[next + 1] = 0

    # 만족도 최대인 사람이 못 먹을 때 -> 양 옆이 먹어야 함

    return answer

solution([5, 4, 4, 6, 2, 1, 3], 3)