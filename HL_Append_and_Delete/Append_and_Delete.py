def solution(s, t, k):
    check= 0

    for i, val in enumerate(s):
        if(i>= len(t)):
            check+= len(s[i:])
            break
        if(val!= t[i]):
            check+= len(s[i:])+ len(t[i:])
            break
        if(i== len(s)- 1 and len(s)< len(t)):
            check+= len(t[i+ 1:])

    print(check)

    if(check> k or abs(check- k)%2 == 1):
        return "No"
    else:
        return "Yes"

print(solution("y", "yu", 2))
print(solution("zzzzz", "zzzzzzz", 4))
print(solution("abcd", "abcdert", 10))