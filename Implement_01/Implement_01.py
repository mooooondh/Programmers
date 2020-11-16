def solution(a, b):
    day= ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month= [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m= sum(month[: a])+ b+ 4

    answer= day[m% 7]

    return answer