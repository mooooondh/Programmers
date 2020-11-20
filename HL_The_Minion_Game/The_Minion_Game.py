
def solution(s):
    vol= ["A", "E", "U", "I", "O"]
    stu, kev= 0, 0

    for i in range(len(s)):
        if s[i] in vol:
            kev+= len(s)- i
        else:
            stu+= len(s)- i

    print(s.count("ANA"))
    print(stu, kev)
    if(stu== kev):
        return "Draw"
    elif(stu> kev):
        return "Stuart "+ str(stu)
    else:
        return "Kevin "+ str(kev)

print(solution("BANANA"))
