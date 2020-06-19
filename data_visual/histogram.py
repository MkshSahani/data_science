# for generation of histogram

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(0, 100, 100)
print(data)

n, bins, patches = plt.hist(data, bins=20)
print(n, bins, patches)
plt.show()
