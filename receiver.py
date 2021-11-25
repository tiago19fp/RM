from os import set_inheritable
from typing import Counter, final
import numpy as np
import pylab as plt

def fun_menos1(array):
    x = 0
    while x < len(array):
        if(array[x] == 0):
            array[x] = -1
        x = x +1
    return array

def fun_zeros(array):
    x = 0
    while x < len(array):
        if(array[x] == -1):
            array[x] = 0
        x = x +1
    return array

def mult_array(arr, chip):
    arraym = [0]*len(arr)
    x = 0
    y = 0
    while x < len(arr):
        if(y==len(chip)):
            y = 0
        arraym[x]= float(arr[x]) * float(chip[y])
        x += 1
        y += 1
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

    x = 0
    multChip = []
    while(x < len(chip)):
        integer_map = map(int, chip[x])
        integer_list = list(integer_map)
        chipMinus1 = fun_menos1(integer_list)
        multChip.append(mult_array(sinal,chipMinus1))
        #print(multChip)
        x += 1

    array = multChip[0]
    finalArray = []
    count = 0
    fim = len(array)
    for n in array:
        if(count == fim):
            break
        soma = float(array[count]) + float(array[count + 1]) + float(array[count + 2])
        if(soma > 0):
            finalArray.append(1)
        else:
            finalArray.append(0)
        count += 3
        soma = 0
