import numpy as np
import matplotlib.pyplot as plt
import math
plt.axis([0, 6, 0, 30])
plt.title("Element adding")
plt.xlabel("Counting", color="gray")
plt.ylabel("Output", color="gray")
plt.text(1, 1.5, "First")
plt.text(2, 4.5, "Second")
plt.text(3, 9.5, "Third")
plt.text(4, 16.5, "Fourth")
plt.text(5, 25.5, "Fifth")
plt.text(2, 20, r"$y = x^2$", bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.grid(True)
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.plot([1, 2, 3, 4, 5], [0.5, 0.9, 1.9, 5, 7], 'g^')
plt.plot([1, 2, 3, 4, 5], [0.2, 0.4, 0.7, 9, 10], 'b*')
plt.legend(['First Series', 'Second Series', 'Third Series'], loc=2)
plt.savefig('first_plot.png')
plt.show()
