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
    k = 0
    tam = 0
    #print(chip)
    while x < len(arr):
        #print("Mensagem: "+str(bitAr[x]))
        while y < 1:
            if(tam == len(chip)):
                tam = 0
            #print(tam + y)
            arraym[k] = float(arr[x]) * float(chip[tam + y])
            #print("Chip: "+str(chip[tam + y]))
            #print("Sinal: "+str(arraym[k]))
            y = y + 1
            k = k + 1
        tam = tam + 1
        #print("-----------")
        #print(tam)
        #print(len(chip))
        #print("-----------")
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
        soma = float(array[count]) + float(array[count + 1]) + float(array[count + 2])+float(array[count+3]) + float(array[count + 4]) + float(array[count + 5])+float(array[count+6]) + float(array[count + 7]) + float(array[count + 8])+float(array[count+9]) + float(array[count + 10]) + float(array[count + 11])+float(array[count+12]) + float(array[count + 13]) + float(array[count + 14])+float(array[count+15])

        if(soma > 0):
            finalArray.append(1)
        else:
            finalArray.append(0)
        count += 16
        soma = 0

    t = 0
    erros = 0
    mess = message[0]

    while t < len(finalArray):
        #print(str(finalArray[t])+"|"+str(mess[t]))
        if(str(finalArray[t])!=str(mess[t])):
            erros += 1
        t = t + 1

    print(erros)
    
