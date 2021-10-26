import numpy as np
import pylab as plt
import bitarray
import random


def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))

def fun_fs(array, fs):
    bitArrayFs = [0]*fs*len(array)
    y = 0
    k = 0
    c = 0
    while y < len(bitArrayFs):
        while k < 5:
            bitArrayFs[y+k] = array[c]
            k = k+1
        y = y + 5
        k = 0
        c = c + 1

    return bitArrayFs

def fun_minus_one(array):
    x = 0
    while x < len(array):
        if(array[x] == 0):
            array[x] = -1
        x = x +1
    return array

def gene_pse(lenArray):
   array = [0]*lenArray
   x = 0
   while x < lenArray: 
           array[x]=random.randint(0, 1) 
           x = x + 1
   return fun_minus_one(array)


if __name__ == "__main__":
    bits = bitarray.bitarray()
    message = "ola"
    bitArray = text_to_bits(message)
    fs = 5
    print(len(bitArray))
    print('-----Array mensagem------')
    bitArray = fun_minus_one(bitArray)
    print(bitArray)
    print('-----Array com fs = 5-------')
    bitArrayf = fun_fs(bitArray, fs)
    print(bitArrayf)
    print('-----Array psd----')
    psd_array = gene_pse(len(bitArrayf)+fs)
    print(psd_array)
    print('-----Array psd com fs = 2------')
    fsp = 2
    psd_array_fs = fun_fs(psd_array,fsp)
    print(psd_array_fs)
    