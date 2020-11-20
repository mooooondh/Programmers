n_set, list_cnt= map(int, input().split())
n= list(map(int, input().split()))
a= set(map(int, input().split()))
b= set(map(int, input().split()))
answer= 0

for i in n:
    if i in a:
        answer+= 1
    if i in b:
        answer-= 1

print(answer)
