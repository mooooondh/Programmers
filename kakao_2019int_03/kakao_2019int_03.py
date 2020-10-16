import itertools
import re

def solution(user_id, banned_id):
    comp_data= []
    case_data= [[] for _ in range(len(banned_id))]

    for i in banned_id:
        data= list(i)
        for j, val in enumerate(data):
            if(val== "*"):
                data[j]= "."
        comp_data.append("".join(data))

    for i, val1 in enumerate(comp_data):
        p= re.compile(val1)
        for j, val2 in enumerate(user_id):
            if(len(val1)== len(val2)):
                m= p.match(val2)

                if(m!= None):
                    case_data[i].append(m[0])

    print(case_data)
    case_list= list(itertools.product(*case_data))

    for i, val in enumerate(case_list):
        case_list[i]= list(case_list[i])
        case_list[i].sort()

    i = 0

    while(True):
        if (len(case_list[i]) != len(list(set(case_list[i])))):
            case_list.pop(i)
        else:
            i+= 1

        if(i== len(case_list)):
            break

    case_list= list(set(map(tuple, case_list)))

    answer= len(case_list)

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))