# 마법의 엘레베이터

# 30.8/100.0
# 정확성 테스트 13개 중 4개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(storey):

    num = list(map(int, str(storey)))   # 숫자 자리수별로 리스트에 넣기
    num.append(0)
    num.append(0)
    answer = 0

    for i in num:
        next_index = num.index(i) + 1

        if i < 5:
            answer += i
        elif i > 5:
            answer += 10 - i
            num[next_index] += 1

            if num[next_index] == 10:
                num[next_index] = 0
                num[next_index + 1] = 1
        else:
            answer += 5

    return answer

solution(16)
