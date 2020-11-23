from itertools import permutations

def solution(numbers):
    num= list(map(str, numbers))
    case= list(permutations(num))
    val= []

    for i in case:
        now_num= ""
        for j in i:
            now_num+= j

        val.append(int(now_num))

    return str(max(val))

print(solution([40, 403]))