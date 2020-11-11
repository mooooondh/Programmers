# BF_03.py

def solution(brown, yellow):
    answer = []
    wh_val= brown//2
    h= 1

    for i in range(wh_val, 2, -1):
        h+= 1
        y_cal= (i- 2)* (h- 2)

        if(y_cal== yellow):
            answer.append(i)
            answer.append(h)
            break

    return answer