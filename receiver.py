from os import set_inheritable
from typing import Counter, final
import numpy as np
import pylab as plt

from scipy.stats import spearmanr


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
        x += 1
    q = 0
    array_media = []
    while q < len(message):
        array = multChip[q]
        #print(array)
        finalArray = []
        count = 0
        fim = len(array)
        f = 0
        while f < len(array):
            t = 0
            while t < fe[0]:
                soma = float(soma) + float(array[f+t])
                t = t + 1
            if(soma > 0):
                finalArray.append(1)
            else:
                finalArray.append(0)
            soma = 0
            f = f + fe[0]

        
        erros = 0
        mess = message[q]
        r = 0
        while r < len(finalArray):
            #print(str(finalArray[r])+"|"+str(mess[r]))
            if(str(finalArray[r])!=str(mess[r])):
                erros += 1
            r = r + 1

        print("----Msg "+str(q+1)+" ----")
        print("Erros:"+str(erros))
        print("BER:"+str(erros/1000))
        array_media.append((erros/1000))
        #x  = 0
        #array_spe = []
        #while x <1000:
        #finalArray = finalArray[-x:] + finalArray[:-x]
        coef, p = spearmanr(mess, finalArray)
        print('Spearmans correlation coefficient: %.3f' % coef)
        #array_spe.append(coef)
        # interpret the significance
        #alpha = 0.05
        #if p > alpha:
            #print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
        #else:
            #print('Samples are correlated (reject H0) p=%.3f' % p)
        q = q + 1
        #x = x + 1
        print('-------------')
            
    print("Mean:"+str(np.mean(array_media)))
