#BF_01.py

def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    stu_sc = [0, 0, 0]
    for i, ans in enumerate(answers):
        if (stu1[i] == ans):
            stu_sc[0] += 1
        if (stu2[i] == ans):
            stu_sc[1] += 1
        if (stu3[i] == ans):
            stu_sc[2] += 1

    for i, sc in enumerate(stu_sc):
        if (sc == max(stu_sc)):
            answer.append(i + 1)

    return answer