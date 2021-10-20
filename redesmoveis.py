import matplotlib.pyplot as plt
import numpy as np
import bitarray

plt.close('all')

message = "Ola tudo bem"
bits = bitarray.bitarray()

bits.frombytes(message.encode('utf-8'))
print(bits)

bits[np.where(bits >= 0.5)] = 1
bits[np.where(bits < 0.5)] = 0

plt.plot(bits)
plt.show()

