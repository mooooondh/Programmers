# hash_02.py

def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if(i== j or len(i)== len(j)):
                continue
            if(j[:len(i)]== i):
                return False
    return True