# heap_01.py

import heapq

def solution(scoville, K):
    answer = 0
    heap= scoville
    heapq.heapify(heap)

    while(heap[0]< K):
        heapq.heappush(heap, (heapq.heappop(heap)+ (heapq.heappop(heap)* 2)))
        answer+= 1
        if(len(heap)== 1 and heap[0]< K):
            return -1

    return answer