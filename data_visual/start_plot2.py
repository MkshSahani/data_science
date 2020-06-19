# keyword arguments in the matplotlib.pyplot.plot(*args, **kwargs)

import numpy as np
import matplotlib.pyplot as plt
import math

# plt.plot([32, 1, 36, 90, 79], 'b', linewidth=4)
# plt.show()

# working on the subplot

input_ = np.arange(0, 5, 0.1)
output_ = np.sin(np.pi * input_ * 2)

plt.subplot(311)
plt.plot(input_, output_, 'b-.')
plt.subplot(312)
plt.plot(input_, output_, 'g--')
plt.subplot(313)
plt.plot(input_, output_, 'r.')
plt.show()
