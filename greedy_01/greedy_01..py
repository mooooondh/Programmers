# greedy_01.py

def solution(n, lost, reserve):
    answer = n
    res= reserve
    lost_stu= []
    los= 0

    for i in lost:
        if i in res:
            res.pop(res.index(i))
        else:
            lost_stu.append(i)


    for i in lost_stu:
        if i- 1 in res:
            res.pop(res.index(i- 1))
        elif i+ 1 in res:
            res.pop(res.index(i+ 1))
        else:
            los+= 1

    answer-= los
    return answer