import threading
import numpy as np


class Train(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            print("Woriking")


t = Train()
t.start()
t.join()
