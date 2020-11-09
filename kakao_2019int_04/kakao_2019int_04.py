import copy

def solution(stones, k):
    left, right= 0, 200000000

    while(left<= right):
        mid= (left+ right)// 2
        bridge= copy.deepcopy(stones)
        count = 0
        check= False

        for i in range(len(bridge)):
            bridge[i]-= mid

        for i in bridge:
            if(i<= 0):
                count+= 1
            else:
                count= 0

            if(count>= k):
                check= True
                break

        if(check== True):
            right= mid- 1
        else:
            left= mid+ 1

    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))