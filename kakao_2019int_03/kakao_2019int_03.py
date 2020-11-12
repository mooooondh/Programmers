from itertools import permutations

def len_check(ban_id, check_id):
    for i in range(len(ban_id)):
        if(len(ban_id[i])!= len(check_id[i])):
            return False
        if(str_check(ban_id[i], check_id[i])== False):
            return False
    return True

def str_check(ban_id, check_id):
    for i in range(len(ban_id)):
        if(ban_id[i]== "*"):
            continue
        elif(ban_id[i]!= check_id[i]):
            return False
    return True

def solution(user_id, banned_id):
    answer = []

    for i in permutations(user_id, len(banned_id)):
        if(len_check(banned_id, i)== True):
            i= set(i)
            if i not in answer:
                answer.append(i)

    return len(answer)
