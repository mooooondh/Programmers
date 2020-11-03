# kaka0_2020int_03.py

def solution(gems):
    end= 0
    kind_gem= list(set(gems))
    gem= [0]+ gems
    answer= [0, 123456]

    check_s, check_e = 0, 0

    for start in range(len(gem)):
        while(len(gem)> end and check_e== 0):
            for i in kind_gem:
                if i in gem[start: end+ 1]:
                    check_e+= 1

            if(check_e!= len(kind_gem)):
                end += 1
                check_e= 0

        if(start<= end and check_e!= 0):
            for i in kind_gem:
                if i not in gem[start: end+ 1] or start== end:
                    if(start== 1):
                        if ((answer[1] - answer[0]) > (end - start)):
                            answer[0] = start
                            answer[1] = end
                    else:
                        if ((answer[1] - answer[0]) > (end - (start- 1))):
                            answer[0] = start- 1
                            answer[1] = end
                    check_s, check_e = 0, 0
                    break
    return answer
