# hash_01.py

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
        pass

    return participant[-1]