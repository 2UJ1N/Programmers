# 체육복

# 58.3/100.0
# 정확성 테스트 12개 중 7개 통과
# 효율성 테스트 5개 중 0개 통과

def solution(n, lost, reserve):
    student = [1] * n

    for i in lost:
        student[i - 1] = 0

    for i in reserve:
        if i == 1:
            if student[i] == 0:
                student[i] = 1
        elif i == n:
            if student[i - 1] == 0:
                student[i - 1] = 1
        else:
            if student[i - 2] == 0:
                student[i - 2] = 1
            elif student[i] == 0:
                student[i] = 1
            else:
                pass

    print(student.count(1))
