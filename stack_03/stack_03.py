from collections import deque

def solution(bridge_length, weight, truck_weights):
    time= 0
    answer= 0
    bridge= deque()

    while(True):
        if (len(truck_weights) == 0 and len(bridge) == 0):
            answer+= 1
            break

        while(len(truck_weights)!= 0 and sum(bridge) + truck_weights[0] <=  weight):
            bridge.append(truck_weights.pop(0))
            time+= 1

        if (time>= bridge_length):
            bridge.popleft()

            if(len(bridge)== 0):
                answer += time
                time= 0
            else:
                answer+= 1
                time-= 1

        else:
            time+= 1

    return answer