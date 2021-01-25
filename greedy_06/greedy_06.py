# greedy_06.py

def solution(n, costs):
    global answer
    answer= 0
    connect= [[] for _ in range(n)]
    check= []

    for i in range(n):
        check.append(i)


    num= 0
    connect_check = []

    while(check!= connect_check):
        num+= 1

        for val in costs:
            if(val[-1]== num):
                connect[val[0]].append(val[1])
                connect[val[1]].append(val[0])
                answer+= val[-1]

        for i in connect:
            for j in i:
                if j not in connect_check:
                    connect_check.append(j)

        connect_check.sort()

    return answer