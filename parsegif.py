# @Fei

import numpy as np

class Stream():
    def __init__(self, data) -> None:
        self.data = data
        self.pos = 0
        self.len = len(data)
        pass

def loadData(path):
    with open(path, "rb") as f:
        data = f.readlines()

loadData("Wax_fire.gif")