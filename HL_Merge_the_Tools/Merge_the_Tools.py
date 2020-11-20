def solution(string, k):
    for i in range(0, len(string), k):
        val= string[i: i+ k]
        check= []
        for j in val:
            if j not in check:
                check.append(j)

        print("".join(check))
    return

solution("AABCAAADA", 3)