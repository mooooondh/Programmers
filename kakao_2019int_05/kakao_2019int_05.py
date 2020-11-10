# kakao_2019int_05.py

# sol#1

# import sys
# sys.setrecursionlimit(10000)
#
# def find_room(check, room):
#     if check not in room.keys():
#         room[check]= check+ 1
#         return check
#
#     fnd_room= find_room(room[check], room)
#     room[check]= fnd_room+ 1
#     return fnd_room
#
#
# def solution(k, room_number):
#     answer= []
#     room= {}
#
#     for i in room_number:
#         empty_room= find_room(i, room)
#         answer.append(empty_room)
#     return answer

# sol#2
def solution(k, room_number):
    answer = []
    room = {}

    for i in room_number:
        n= i
        visit= [n]

        while n in room:
            n= room[n]
            visit.append(n)

        answer.append(n)

        for j in visit:
            room[j]= n+ 1

    return answer