from typing import Counter
import numpy as np
import pylab as plt

def fun_menos1(array):
    x = 0
    while x < len(array):
        if(array[x] == 0):
            array[x] = -1
        x = x +1
    return array

def mult_array(arr, chip):
    arraym = [0]*len(arr)
    x = 0
    y = 0
    k = 0
    l = 0
    while x < len(arr):
        while y < 1:
            if(y + l > len(chip)):
                l = 0
            arraym[k] = arr[x] * chip[y + l]
            y = y + 1
            k = k + 1
        l = y
        y = 0
        x = x + 1
    return arraym

if __name__ == "__main__":
    channel = "channel.txt"
    with open(channel, "r") as filestream: 
        lines = filestream.readlines()
        count = 0
        firstTime = 0
        message = []
        chip = []
        fe = []

        for line in lines:
            count += 1
            if(firstTime == 0):
                if(count % 4 == 1):   # 1st line  (sinal)
                    sinal = lines[count-1].strip().split(',')
                if(count % 4 == 2):   # 2nd line  (message)
                    message.append(lines[count-1].strip().split(','))
                if(count % 4 == 3):   # 3rd line  (chip)
                    chip.append(lines[count-1].strip().split(','))
                if(count % 4 == 0):   # 4th line  (fe)
                    fe.append(int(lines[count-1].strip()))
                    firstTime = 1
                    count = 4
            else:
                if(count % 3 == 2):   # 5th/8th/... line  (message)
                    message.append(lines[count-1].strip().split(','))
                if(count % 3 == 0):   # 6th/9th/... line  (chip)
                    chip.append(lines[count-1].strip().split(','))
                if(count % 3 == 1):   # 7th/10th/... line  (fe)
                    fe.append(int(lines[count-1].strip()))

    soma = 0
    count = 0
    fim = len(sinal)
    finalArray = []
    for n in sinal:
        if(count == fim):
            break
        soma = float(sinal[count]) + float(sinal[count + 1])
        if(soma > 0):
            finalArray.append(1)
        else:
            finalArray.append(0)
        count += 2
        soma = 0
    arrayMinus1 = fun_menos1(finalArray)
    
    multChip = []
    x = 0
    while(x < len(chip)):
        integer_map = map(int, chip[x])
        integer_list = list(integer_map)
        chipMinus1 = fun_menos1(integer_list)
        multChip.append(mult_array(arrayMinus1,chipMinus1))
        x += 1
    print(multChip)