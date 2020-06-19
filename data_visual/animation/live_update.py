import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd


# plt.plot(keys, values)
# plt.show()

figure = plt.figure()

ax1 = figure.add_subplot(1, 1, 1)


def animate(i):
    data = pd.read_csv('live_update_data.csv')
    print(data)
    data = pd.DataFrame(data)
    print("==== this is data frame ====")
    print(data)
    print("'=== this is data frame ===")

    keys = data.iloc[:, 0].values
    print("Keys : ", keys)
    values = data.iloc[:, 1].values
    print("values : ", values)

    ax1.clear()
    ax1.plot(keys, values, 'r', linewidth=5)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Live Graph")


ani = animation.FuncAnimation(figure, animate, interval=500)
plt.show()
