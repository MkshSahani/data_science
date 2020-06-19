# for learning about matplotlib

import numpy as np
import matplotlib.pyplot as plt

input_1 = [i for i in range(1, 20)]
output_2 = [2 * i + 1 for i in input_1]
print(input_1)
print(output_2)

plt.plot(input_1, output_2)
plt.show()
