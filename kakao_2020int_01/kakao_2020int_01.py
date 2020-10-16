# kaka0_2020int_01.py

def solution(numbers, hand):
    phone= [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [2, 3]]
    ans= []
    position= [10, 11]

    for i in numbers:
        if (i == 1 or i == 4 or i == 7):
            ans.append("L")
            position[0]= i
            continue
        if(i== 3 or i== 6 or i== 9):
            ans.append("R")
            position[1]= i
            continue

        x_left= abs(phone[position[0]][0]- phone[i][0])
        y_left= abs(phone[position[0]][1]- phone[i][1])
        dis_left= x_left+ y_left

        x_right = abs(phone[position[1]][0] - phone[i][0])
        y_right = abs(phone[position[1]][1] - phone[i][1])
        dis_right = x_right + y_right

        if(dis_left> dis_right):
            position[1]= i
            ans.append("R")
        elif(dis_left< dis_right):
            position[0]= i
            ans.append("L")
        else:
            if(hand== "left"):
                position[0]= i
                ans.append("L")
            else:
                position[1]= i
                ans.append("R")

    answer= "".join(ans)

    return answer



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))