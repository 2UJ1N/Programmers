# 큰 수 만들기

# 16.7/100.0
# 정확성 테스트 12개 중 2개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(number, k):

    answer = 0
    word1 = list(number)
    word = list(map(int, word1))

    while k > 0:
        for i in range(0, 10):
            while i in word:
                if k <= 0:  # 왜 while문이 동작하지 않을까
                    break
                word.remove(i)
                k -= 1
                print(word)

        if k == 0:  # 왜 while문이 동작하지 않을까
            break

    answer = ''.join(map(str, word))

    return answer

solution("1924", 2)