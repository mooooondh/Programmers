# stack_02.py

from collections import deque


def solution(progresses, speeds):
    answer = []
    spen_days = deque()

    for i in range(len(progresses)):
        for j in range(101):
            if (j > (99 - progresses[i]) / speeds[i]):
                spen_days.append(j)
                break

    spen_days.append(101)

    while (True):
        if (len(spen_days) <= 1):
            break

        val = spen_days.popleft()
        service = 1

        for i in range(len(spen_days)):
            if (spen_days[i] > val):
                for _ in range(i):
                    spen_days.popleft()
                break
            service += 1

        answer.append(service)

    return answer