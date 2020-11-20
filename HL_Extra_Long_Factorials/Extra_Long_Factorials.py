def fact(n):
    if(n== 1):
        return 1
    return n* fact(n- 1)

def solution(n):
    print(fact(n))
    return

solution(25)