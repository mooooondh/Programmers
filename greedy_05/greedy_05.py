# greedy_05.py

def solution(s):
    check= []

    for i in range(len(s)):
        check.append(s[i])
        if(len(check)>= 2 and check[-1]== check[-2]):
            check.pop()
            check.pop()

    if(len(check)== 0):
        return 1
    else:
        return 0