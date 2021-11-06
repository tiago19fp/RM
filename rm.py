import numpy as np
import matplotlib.pyplot as plt
import bitarray
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

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

if __name__ == "__main__":
    bits = bitarray.bitarray()
    message = "ola"
    bitArray = text_to_bits(message)                            # Mensagem para bits
    fs = 4                                                      # Frequência de amostragem
    #print(len(bitArray))
    #print('-----Array mensagem------')
    bitArray = fun_menos1(bitArray)                             # Transformar os zeros em menos 1
    #print(bitArray)
    #print(bitArray)
    #print('-----Array com fs = 5-------')
    bitArrayf = np.repeat(bitArray, fs)
    t = 0.5 * np.arange(len(bitArrayf))
    #print(bitArrayf)
    #print(bitArrayf)
    #print('-----Array psd----')
    fsp = 2  
    psd_array = pseudo_generator(int(len(bitArrayf)/fsp))          # Gerar o pseudo noise
    #print(psd_array)
    #print('-----Array psd com fs = 2------')                      # Frequência do pseudo noise
    psd_array_fs = np.repeat(psd_array, fs)                        # Multiplicar o pseudo pela Fs
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
        

    graph_mens = np.array(bitArray)                     # Array de bits para gerar o gráfico mensagem sem Fs      
    graph_mensFs = np.array(bitArrayf)                          # Array de bits para gerar o gráfico mensagem com Fs     
    graph_pseudo = np.array(psd_array)                          # Array de bits para gerar o gráfico do pseudo noise
    graph_pseudoFs = np.array(psd_array_fs)                     # Array de bits para gerar o gráfico do pseudo com Fs  

    print(graph_mens)
    print(graph_pseudo)
    
    #my_lines('x', range(10), color='.5', linewidth=2)
    #my_lines('y', [0.5, 2, 4], color='.5', linewidth=2)

    #plt.step(t, graph_mens + 0, 'r', linewidth = 2, where='post')
    #plt.step(t, graph_mensFs + 2, 'r', linewidth = 2, where='post')
    #plt.ylim([-1,6])

    for tbit, bit in enumerate(bitArray):
        plt.text(tbit + 0.5, 1.5, str(bit))

    #plt.gca().axis('off')
    #plt.show()
    