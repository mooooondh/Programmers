def solution(t1, t2):
    time = 0

    if(t1[: 24]== t2[: 24]):
        time+= int(t1[-4: -2])* 3600+ int(t1[-2:])* 60
        print(time)
        return

    if(t1[4: 6]!= t2[4: 6]):
        time+= (int(t1[4: 6])- int(t2[4: 6]))* 24* 3600
    if(t1[16: 18]!= t2[16: 18]):
        time+= (int(t1[16: 18])- int(t2[16: 18]))* 3600
    if(t1[19: 21] != t2[19: 21]):
        time += (int(t1[19: 21]) - int(t2[19: 21])) * 60

    time-= int(t1[-4:-2])* 3600+ int(t1[-2: ])* 60

    print(time)
    return

solution("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
solution("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000")