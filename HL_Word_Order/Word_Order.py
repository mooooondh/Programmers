n= int(input())
words= {}

for i in range(n):
    input_data= str(input())
    if input_data in words.keys():
        words[input_data]+= 1
    else:
        words[input_data]= 1

print(len(words))

for i in words.values():
    print(i, end= " ")
