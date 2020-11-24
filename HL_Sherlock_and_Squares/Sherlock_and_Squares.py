def solution(a, b):
    answer= 0
    num =1

    while(num* num< a):
        num+= 1
    while(num* num<= b):
        answer+= 1
        num+= 1

    return answer

print(solution(3, 9))