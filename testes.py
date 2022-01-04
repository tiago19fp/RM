
from scipy.linalg import hadamard
import numpy as np

import numpy as np

array = np.array([1,2,3,4,5])
x = 0
while x < 5:
    array_new = np.roll(array, x)
    print(array_new)
    x = x + 1


