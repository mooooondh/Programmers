import bisect

def solution(ranked, player):
    rank= sorted(set(ranked))
    print(rank)

    for i in player:
        print(len(rank)+ 1- bisect.bisect_right(rank, i))
    return

print(solution([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))