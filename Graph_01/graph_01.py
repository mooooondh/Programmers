from collections import deque

def bfs(position, graph, distance):
    que= deque()
    que.append(position)

    while(que):
        now= que.popleft()
        for i in graph[now]:
            if(distance[i]== 0):
                que.append(i)
                distance[i]= distance[now]+ 1

    return distance

def solution(n, edge):
    graph= [[] for _ in range(n+ 1)]
    distance= [0]* (n+ 1)
    distance[1]= 1

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    bfs(1, graph, distance)

    max_val= max(distance)
    answer= distance.count(max_val)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))