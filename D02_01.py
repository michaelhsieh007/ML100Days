# -*- coding: utf-8 -*-
import numpy as np
array2 = np.array(range(30))
print(array2)
array2.reshape((5, 6), order='F')
print(array2)
print(np.where(array2 % 6 == 1))