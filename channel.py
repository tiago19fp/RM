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
            cdma = lines[count-1].strip().split(',')
            cdma = cdma[:-1]
        if(count % 4 == 3):   # 3rd line  (chip)
            chip = lines[count-1].strip().split(',')
            chip = chip[:-1]
        if(count % 4 == 0):   # 4th line  (fe)
            fe = lines[count-1]

    return cdma,chip,fe

if __name__ == "__main__":

    ficheiros = []
    f_atenuacao = []
    configFile = "configFile.txt"
    output = ''
    nFile = 0
    desvio = 0
    noise = ''

    with open(configFile, "r") as filestream:                         # OPEN CONFIG FILE
        counter = 0
        for line in filestream:
            counter += 1
            if(counter % 4 == 1):   # 1st line
                ficheiros = line.strip().split(",")
            if(counter % 4 == 2):   # 2nd line
                f_atenuacao = line.strip().split(",")
            if(counter % 4 == 3):   # 3rd line
                output = line.strip()
            if(counter % 4 == 0):   # 4th line
                desvio = int(line.strip())

    stream = open(output,"w")
    finalSignal = [0] * 100

    for i in ficheiros:                                                     
        with open(ficheiros[nFile], "r") as filestream:                     # OPEN FILES FROM CONFIG FILE
            cdma,chip,fe = getAttributes(filestream)
            noise = np.random.normal(0, desvio, len(cdma))
            arrayAtenuado = [0] * len(cdma)
            counter = 0
            for x in cdma:
                arrayAtenuado[counter] = float(f_atenuacao[nFile]) * float(cdma[counter])
                counter += 1
            finalSignal = finalSignal + arrayAtenuado
            # signal = arrayAtenuado + noise
        nFile += 1
        
    finalSignal = finalSignal + noise
    print(finalSignal)


    # for listitem in signal:
    #             stream.write('%s,' % listitem) 
    #         stream.write('\n')
    #         for listitem in chip:
    #             stream.write('%s,' % listitem)   
    #         stream.write('\n')
    #         stream.write(str(fe))
    #         stream.write('\n')
