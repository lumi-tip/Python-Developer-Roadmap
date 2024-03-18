list = [2,343,5,234,6,45,7,565,23]

def insertion_sort(inputlist):
    for i in range(1, len(inputlist)):
        j = i - 1
        nxt_element = inputlist[i]
    
    while (inputlist[j] > nxt_element) and (j >= 0):
        inputlist[j+1] = inputlist[j]
        j = j - 1
    inputlist[j + 1] = nxt_element