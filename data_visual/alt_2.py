import numpy as np
import matplotlib.pyplot as plt
import math

input_1 = np.arange(0, 2.5, 0.1)
output_1 = np.array(list(map(math.sin, math.pi * input_1)))
output_2 = np.array(list(map(math.sin, math.pi * input_1 + math.pi * 1 / 2)))
output_3 = np.array(list(map(math.sin, math.pi * input_1 - math.pi - 1 / 2)))
plt.title("Alternative plot")
plt.plot(input_1, output_1, 'b--', input_1,
         output_2, 'g', input_1, output_3, 'y-')
plt.show()
