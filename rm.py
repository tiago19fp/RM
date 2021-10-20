import numpy as np
import pylab as plt
import bitarray

def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))

bits = bitarray.bitarray()
message = "ola"

bitArray = text_to_bits(message)
print(bitArray)

bit = np.array(bitArray)
plt.step(np.arange(0,len(bit)),bit)