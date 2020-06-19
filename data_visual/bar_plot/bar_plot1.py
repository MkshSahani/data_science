# bar plot

import matplotlib.pyplot as plt
import numpy as np

index = np.arange(4)
plt.bar(index, [3, 5, 1, 9], color='g')
plt.xticks(index, ['A', 'B', 'C', 'D'])
plt.show()
