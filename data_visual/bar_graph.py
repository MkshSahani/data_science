# bar_graph.py

import numpy as np
import matplotlib.pyplot as plt

# index values for the bar plot.
index = np.arange(5)

# values with resepect to each index.
values = [4, 3, 1, 8, 3]

plt.bar(index, values, 'g')
plt.show()

# this is difference.
