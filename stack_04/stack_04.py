# stack_04.py

def sort_print(ready):
    check= False

    while(check== False):
        pop_data= ready[0]
        check= True

        for i in ready:
            if(pop_data[0]< i[0]):
                pop_data= ready.pop(0)
                ready.append(pop_data)
                check= False
                break
    return ready

def solution(priorities, location):
    answer = 1
    set_loc = [i for i in range(len(priorities))]

    printer= list(zip(priorities, set_loc))

    while(True):
        printer= sort_print(printer)

        printing= printer.pop(0)

        if(printing[1]== location):
            return answer
        else:
            answer+= 1