# kakao_2019int_02

def solution(s):
    answer = []
    data= s[1:-1]
    arr = []
    pre_ans= []
    num= []
    check = False

    for i in data:
        if(i== "{"):
            check= True
            continue
        if(i== "}"):
            arr.append(int("".join(num)))
            num = []
            pre_ans.append(arr)
            arr= []
            check= False
            continue
        if(i== "," and len(num)!= 0):
            arr.append(int("".join(num)))
            num = []
            continue
        if(check== True):
            num.append(i)

    pre_ans.sort(key= len)

    for i in pre_ans:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer