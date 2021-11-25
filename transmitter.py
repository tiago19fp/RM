import numpy as np
import pylab as plt
import bitarray
import random
import sys

def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))

def fun_fs(array, fs):
    bitArrayFs = [0]*fs*len(array)
    y = 0
    k = 0
    c = 0
    while y < len(bitArrayFs):
        while k < fs:
            bitArrayFs[y+k] = array[c]
            k = k+1
        y = y + fs
        k = 0
        c = c + 1
    return bitArrayFs

def fun_menos1(array):
    x = 0
    while x < len(array):
        if(array[x] == 0):
            array[x] = -1
        x = x +1
    return array

def retirar_menos1(array):
    x = 0
    while x < len(array):
        if(array[x] == -1):
            array[x] = 0
        x = x +1
    return array

def pseudo_generator_message(lenArray):
   array = [0]*lenArray
   x = 0
   while x < lenArray: 
       array[x]=random.randint(0, 1) 
       x = x + 1
   return array

def mult_array(bitAr, chip, fe):
    arraym = [0]*len(bitAr)*fe
    x = 0
    y = 0
    k = 0
    l = 0
    tam = 0
    print(chip)
    while x < len(bitAr):
        #print("Mensagem: "+str(bitAr[x]))
        while y < fe:
            if(tam == len(chip)):
                tam = 0
            #print(tam + y)
            arraym[k] = bitAr[x] * chip[tam + y]
            #print("Chip: "+str(chip[tam + y]))
            #print("Sinal: "+str(arraym[k]))
            y = y + 1
            k = k + 1
        tam = tam + fe
        #print("-----------")
        #print(tam)
        #print(len(chip))
        #print("-----------")
        y = 0
        x = x + 1
    return arraym

if __name__ == "__main__":
    bitArray = pseudo_generator_message(1000000) 
    bitArraymenos1 = bitArray
    fe = int(sys.argv[1])                                                      # Frequência de amostragem
    bitArraymenos1 = fun_menos1(bitArraymenos1)                             # Transformar os zeros em menos 1
    fa = int(sys.argv[2]) 
    psd_array = pseudo_generator_message(random.randint(1,10))                # Gerar o pseudo noise
    #print(psd_array)
    psd_array_fa = fun_fs(psd_array,fa)                        # Multiplicar o pseudo pela Fs4
    #print(psd_array)
    #print(psd_array_fa)
    psd_array_save_file = fun_fs(psd_array,fa)
    #print(psd_array_save_file)
    psd_array_fa = fun_menos1(psd_array_fa)
    toOpen = sys.argv[3]

    #print(len(bitArray))    
    #print(len(psd_array))     
    #print(len(psd_array_fa)) 

    cdma = mult_array(bitArraymenos1, psd_array_fa, fe)
    
    #print(bitArray)
    #print(psd_array_fa)
    #print(len(cdma))

    bitArrayFile = retirar_menos1(bitArraymenos1)
    #print(cdma)
    with open(toOpen, 'w') as filehandle:
        x = 1
        for listitem in cdma:
            if(len(cdma) == x):
                filehandle.write('%s' % listitem) 
                break
            filehandle.write('%s,' % listitem)
            x = x + 1 
        filehandle.write('\n')
        x=1 
        for listitem in bitArrayFile:
            if(len(bitArrayFile) == x):
                filehandle.write('%s' % listitem) 
                break
            filehandle.write('%s,' % listitem) 
            x = x + 1
        filehandle.write('\n')
        x=1
        for listitem in psd_array_save_file:
            if(len(psd_array_save_file) == x):
                filehandle.write('%s' % listitem)
                break 
            filehandle.write('%s,' % listitem)
            x = x + 1
        filehandle.write('\n')
        x=1   
        filehandle.write(str(fe))

    graph_mens = np.array(bitArray)                             # Array de bits para gerar o gráfico mensagem sem Fs      
    graph_pseudo = np.array(psd_array)                          # Array de bits para gerar o gráfico do pseudo noise
    graph_pseudoFs = np.array(psd_array_fa)                     # Array de bits para gerar o gráfico do pseudo com Fs  

    # plt.step(np.arange(0,len(graph_mens)),graph_mens)           # Plot do gráfico mensagem
    # #plt.step(np.arange(0,len(graph_mensFs)),graph_mensFs)      # Plot do gráfico mensagem com Fs
    # plt.step(np.arange(0,len(graph_pseudo)),graph_pseudo)       # Plot do gráfico pseudo 
    # plt.step(np.arange(0,len(graph_pseudoFs)),graph_pseudoFs)   # Plot do gráfico pseudo com Fs
    # plt.legend()
    # plt.show()
