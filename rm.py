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

def pseudo_generator(lenArray):
   array = [0]*lenArray
   x = 0
   while x < lenArray: 
       array[x]=random.randint(0, 1) 
       x = x + 1
   return fun_menos1(array)

def mult_array(array1, array2):
    x = 0
    arraym = [0]*len(array1)
    while x < len(array1):
        arraym[x] = array1[x]*array2[x]
        x = x + 1 
    return arraym



if __name__ == "__main__":
    bits = bitarray.bitarray()
    message = "ola"
    bitArray = text_to_bits(message)                            # Mensagem para bits
    fs = 4                                                      # Frequência de amostragem
    #print(len(bitArray))
    #print('-----Array mensagem------')
    bitArray = fun_menos1(bitArray)                             # Transformar os zeros em menos 1
    #print(bitArray)
    #print('-----Array com fs = 5-------')
    bitArrayf = fun_fs(bitArray, fs)                            # Multiplicar pela frequência de amostragem
    #print(bitArrayf)
    #print('-----Array psd----')
    fsp = 2  
    psd_array = pseudo_generator(int(len(bitArrayf)/fsp))                # Gerar o pseudo noise
    #print(psd_array)
    #print('-----Array psd com fs = 2------')                                                   # Frequência do pseudo noise
    psd_array_fs = fun_fs(psd_array,fsp)                        # Multiplicar o pseudo pela Fs
    #print(psd_array_fs)
    print(len(bitArray))    
    print(len(bitArrayf))     
    print(len(psd_array))     
    print(len(psd_array_fs)) 

    sinal_transmitido = mult_array(bitArrayf, psd_array_fs)

    with open('output.txt', 'w') as filehandle:
        for listitem in sinal_transmitido:
            filehandle.write('%s,' % listitem) 
        filehandle.write('\n')
        for listitem in bitArray:
            filehandle.write('%s,' % listitem) 
        filehandle.write('\n')
        for listitem in psd_array_fs:
            filehandle.write('%s,' % listitem)   
        filehandle.write('\n')
        filehandle.write(str(fs/fsp))
        


    print(sinal_transmitido)
    print(len(sinal_transmitido))
    graph_mens = np.array(bitArray)                             # Array de bits para gerar o gráfico mensagem sem Fs      
    graph_mensFs = np.array(bitArrayf)                          # Array de bits para gerar o gráfico mensagem com Fs     
    graph_pseudo = np.array(psd_array)                          # Array de bits para gerar o gráfico do pseudo noise
    graph_pseudoFs = np.array(psd_array_fs)                     # Array de bits para gerar o gráfico do pseudo com Fs  
    
    plt.step(np.arange(0,len(graph_mens)),graph_mens)           # Plot do gráfico mensagem
    plt.step(np.arange(0,len(graph_mensFs)),graph_mensFs)       # Plot do gráfico mensagem com Fs
    plt.step(np.arange(0,len(graph_pseudo)),graph_pseudo)       # Plot do gráfico pseudo 
    plt.step(np.arange(0,len(graph_pseudoFs)),graph_pseudoFs)   # Plot do gráfico pseudo com Fs
    plt.legend()
    plt.show()
    