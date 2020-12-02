# BF_04.py

def solution(n):
    fib= [1, 1]

    if(n<= 2):
        return 1

    for i in range(2, n):
        fib.append(fib[i- 1]+ fib[i- 2])

    return fib[-1]%1234567