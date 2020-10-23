# DP_01.py

def solution(n):
    if (n <= 3):
        return n

    answer = [0]* (n+1)
    answer[1]= 1
    answer[2]= 2
    answer[3]= 3

    for i in range(4, n+1):
        answer[i]= int((answer[i-1]% 1000000007+ answer[i-2]% 1000000007)%1000000007)

    return answer[n]