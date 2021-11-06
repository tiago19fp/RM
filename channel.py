import numpy as np
import sys
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

if __name__ == "__main__":

    message = sys.argv[1]
    bitArray = text_to_bits(message)                    # Mensagem para bits
    bitArray = fun_menos1(bitArray)
    noise = np.random.normal(0, 1, len(bitArray))
    atenuacao = random.random()
    arrayAtenuado = [0] * len(bitArray)
    for x in bitArray:
        arrayAtenuado[x] = atenuacao * bitArray[x]
        print(arrayAtenuado[x])
        
    signal = arrayAtenuado + noise
    print(bitArray)
    print(arrayAtenuado)
    print(noise)
    print(signal)
