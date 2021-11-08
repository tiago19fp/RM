import numpy as np
import random

def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))

def fun_menos1(array):
    x = 0
    while x < len(array):
        if(array[x] == 0):
            array[x] = -1
        x = x +1
    return array

def getAttributes(ficheiro):
    lines = ficheiro.readlines() 
    count = 0
    for line in lines:
        count += 1
        if(count % 4 == 1):   # 1st line  (sinal)
            bitArray = lines[count-1].strip().split(',')
            bitArray = bitArray[:-1]
        if(count % 4 == 3):   # 3rd line  (chip)
            chip = lines[count-1].strip().split(',')
            chip = chip[:-1]
        if(count % 4 == 0):   # 4th line  (fe)
            fe = lines[count-1]

    return bitArray,chip,fe

if __name__ == "__main__":

    ficheiros = []
    configFile = "configFile.txt"
    output = ''
    nFile = 0
    desvio = 0

    with open(configFile, "r") as filestream:                         # OPEN CONFIG FILE
        counter = 0
        for line in filestream:
            counter += 1
            if(counter % 3 == 1):   # 1st line
                ficheiros = line.strip().split(",")
            if(counter % 3 == 2):   # 2nd line
                output = line.strip()
            if(counter % 3 == 0):   # 2nd line
                desvio = int(line.strip())

    stream = open(output,"w")

    for i in ficheiros:                                                     
        with open(ficheiros[nFile], "r") as filestream:                     # OPEN FILES FROM CONFIG FILE
            bitArray,chip,fe = getAttributes(filestream)
            noise = np.random.normal(0, desvio, len(bitArray))
            atenuacao = random.random()
            arrayAtenuado = [0] * len(bitArray)
            counter = 0
            for x in bitArray:
                arrayAtenuado[counter] = atenuacao * float(bitArray[counter])
                counter += 1
            signal = arrayAtenuado + noise
            print(signal)

            for listitem in signal:
                stream.write('%s,' % listitem) 
            stream.write('\n')
            for listitem in chip:
                stream.write('%s,' % listitem)   
            stream.write('\n')
            stream.write(str(fe))
            stream.write('\n')
        nFile += 1
   
