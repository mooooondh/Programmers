def solution(routes):
    answer= 1
    routes.sort()
    cam = routes[0][1]

    routes.pop(0)

    for i in routes:
        print("Cam: ", cam)
        if(i[0]<= cam):
            cam = min(cam, i[1])
        else:
            cam = i[1]
            answer += 1
    return answer