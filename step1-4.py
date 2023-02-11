# 자전거 공장

# 0/100.0
# 정확성 테스트 14개 중 0개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(cost, order):
    elect = []
    money = []
    month = []
    bicycle = []

    for i in cost:
        elect.append(i[0])f
        money.append(i[1])

    for i in order:
        month.append(i[0])
        bicycle.append(i[1])

    result = [elect[1]] * max(month)   # 최대 월 저장 - 한 달에 얼마씩 생산할건지 넣기
    final = [50] * max(month)

    for i in bicycle:
        amount = i #100
        for j in month:
            check = result[:j - 1]

            for k in check:
                amount -= k

                if amount == 0:
                    for l in range(len(check)):
                        result[l] = 0
                        final[l] = check[l]
                    break

            if amount <= 50:
                result[j - 1] += amount
                final[j - 1] = result[j - 1]

            elif amount <= 100:
                amount2 = amount //2
                result[j - 1] += amount2
                result[j - 2] += amount2
                final[j - 1] += result[j - 1]
                final[j - 2] += result[j - 2]

            print(final)

            


    answer = 0
    return answer

#solution([[0, 10], [50, 20], [100, 30], [200, 40]], [[3, 50], [7, 200], [8, 200]])
solution([[0, 10], [50, 20]], [[3, 100], [4, 200]])