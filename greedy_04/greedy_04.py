import math

def solution(people, limit):
    answer = 0
    weight= sorted(people, reverse= True)
    end= len(weight)- 1

    for i in range(len(weight)):
        if(weight[i]+ weight[end]<= limit):
            end-= 1
            answer+= 1
        else:
            answer+= 1
        if (end <= i):
            break

    return answer