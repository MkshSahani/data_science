# pie chart

import matplotlib.pyplot as plt
import numpy as np

labels = ['Nokia', 'Samsung', 'Apple', 'Lumina']
values = [10, 30, 45, 15]
colors = ['yellow', 'green', 'red', 'blue']
explode = [0.3, 0, 0, 0]
plt.title("Pie Chart")
plt.pie(values, labels=labels, colors=colors,
        explode=explode, startangle=180, shadow=True)
plt.axis('equal')
plt.show()
