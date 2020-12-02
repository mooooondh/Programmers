#
# def fiv(num):
#     if(num<= 2):
#         return 1
#     else:
#         return fiv(num- 1)+ fiv(num- 2)

def solution(n):
    fib= [1, 1]

    if(n<= 2):
        return 1

    for i in range(2, n):
        fib.append(fib[i- 1]+ fib[i- 2])

    return fib[-1]%1234567

print(solution(3))