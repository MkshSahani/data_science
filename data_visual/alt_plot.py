import numpy as np
import matplotlib.pyplot as plt
import math

input_1 = [i for i in range(1, 20)]
output_2 = [2 * i + 1 for i in input_1]
print(input_1)
print(output_2)

plt.plot(input_1, output_2, 'ro')
plt.show()

input_1 = np.arange(0, 2.5, 0.1)
output_1 = np.array(list(map(math.sin, math.pi * input_1)))
output_2 = np.array(list(map(math.sin, math.pi * input_1 + math.pi * 1 / 2)))
output_3 = np.array(list(map(math.sin, math.pi * input_1 - math.pi - 1 / 2)))
plt.title("Alternative plot")
plt.plot(input_1, output_1, 'b*', input_1,
         output_2, 'g^', input_1, output_3, 'ys')
plt.show()
