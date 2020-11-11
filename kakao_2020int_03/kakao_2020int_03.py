# kakao_2020int_03.py

def solution(gems):
    answer= [0, 123456]
    kind_gem= len(set(gems))
    start, end= 0, 0
    dict_gem= {gems[0]: 1}

    while(start< len(gems) and end< len(gems)):
        if(len(dict_gem)== kind_gem):
            if(answer[1]- answer[0]> end- start):
                answer[0]= start
                answer[1]= end
            if(dict_gem[gems[start]]== 1):
                del dict_gem[gems[start]]
            else:
                dict_gem[gems[start]]-= 1
            start+= 1
        else:
            end+= 1
            if(end== len(gems)):
                break
            else:
                if(dict_gem.get(gems[end]) is None):
                    dict_gem[gems[end]]= 1
                else:
                    dict_gem[gems[end]]+= 1

    answer[0]+= 1
    answer[1]+= 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
