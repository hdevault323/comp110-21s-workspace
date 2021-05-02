"""Some examples with numpy ig."""


import numpy as np

x = np.arange(1, 5)
print(x.std())
print(x)
print(x * 2)
print(x % 2 == 1)
print(x[x % 2 == 1])
print(x.std())
