import itertools
import copy

def solution(expression):
    case= list(itertools.permutations(["+", "-", "*"], 3))
    test= []
    num= []
    check_arr= []

    for i in expression:
        if(i== "+" or i== "-"or i== "*"):
            test.append(int("".join(num)))
            test.append(i)
            num= []
        else:
            num.append(i)
    test.append(int("".join(num)))

    test_re= copy.deepcopy(test)

    k= -1

    for i in case:
        for j in i:
            while(k < len(test_re)):
                if(test_re[k]== j):
                    result= 0
                    if(j== "+"):
                        result = test_re[k - 1] + test_re[k + 1]
                    elif(j== "-"):
                        result = test_re[k - 1] - test_re[k + 1]
                    else:
                        result = test_re[k - 1] * test_re[k + 1]
                    test_re[k]= result
                    test_re.pop(k+1)
                    test_re.pop(k-1)

                else:
                    k+=1
            k= -1
        check_arr.append(abs(test_re[0]))
        test_re= copy.deepcopy(test)

    answer= max(check_arr)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))