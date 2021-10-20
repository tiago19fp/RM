import numpy as np
from matplotlib.pyplot import step, show
import matplotlib.pyplot as plt
import bitarray 

def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))


message = 'ola'

y = text_to_bits(message)
print(y)

x = len(y)

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
plt.ylim(-2,2)

plt.xlim(1,24)
 
plt.xlabel('x - axis')

plt.ylabel('y - axis')
 
plt.title('Some cool customizations!')
 
plt.show()