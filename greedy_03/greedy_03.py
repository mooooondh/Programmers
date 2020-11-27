def solution(number, k):
    answer= ""
    start= 0
    num_id= 0
    num= 0

    for i in range(len(number)- k):
        num= number[start]
        num_id= start

        for j in range(start, i+ k+ 1):
            if(num< number[j]):
                num= number[j]
                num_id= j

        start= num_id+ 1
        answer+= num
    return answer