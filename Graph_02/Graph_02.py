def dfs(graph, visit, com, ans):
    visit[com]= True
    ans+= 1

    for i in graph[com]:
        if(visit[i]!= True):
            dfs(graph, visit, i, ans)
    return ans


def solution(n, computers):
    if(n== 1):
        return 1

    answer = 0
    net= computers
    visited= [False]* n
    start= -1

    for i in range(n):
        if(net[i].count(1)== 1):
            net[i]= [999]* n
            answer+= 1
        else:
            net[i][i]= 999
            for j, val in enumerate(net[i]):
                if(val== 1):
                    net[i][j]= j
                    if(start== -1):
                        start= j
                elif(val== 0):
                    net[i][j]= 999
        k= 0
        while(999 in net[i]):
            if(net[i][k]== 999):
                net[i].pop(k)
            else:
                k+= 1

    answer= dfs(net, visited, start, answer)

    return answer