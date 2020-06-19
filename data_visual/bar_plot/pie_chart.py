# pie chart

import numpy as np
import matplotlib.pyplot as plt

labels = ['Nokia', 'Samsung', 'Apple', 'Lumina']
values = [10, 30, 45, 15]
colors = ['yellow', 'green', 'red', 'blue']

plt.pie(values, labels=labels, colors=colors)
plt.show()
