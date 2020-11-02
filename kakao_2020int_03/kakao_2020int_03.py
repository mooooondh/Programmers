# kaka0_2020int_03.py

def solution(gems):
    end= 0
    s_e_point= []
    kind_gem= sorted(list(set(gems)))
    gem= [0]+ gems
    answer= [0, 100001]

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
                        s_e_point.append(start)
                    else:
                        s_e_point.append(start- 1)
                    s_e_point.append(end)
                    check_s, check_e = 0, 0
                    break

    for i in range(0, len(s_e_point), 2):
        if((answer[1]- answer[0])> (s_e_point[i+ 1]- s_e_point[i])):
            answer[0]= s_e_point[i]
            answer[1]= s_e_point[i+ 1]

    return answer





print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
