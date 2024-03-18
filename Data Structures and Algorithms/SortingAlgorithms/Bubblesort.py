list = [2,343,5,234,6,45,7,565,23]

def bublesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for i in range(iter_num):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

bublesort(list)
print(list)