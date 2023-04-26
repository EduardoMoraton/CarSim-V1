import numpy as np

class DNA:
    def __init__(self, size):
        self.instr = np.random.uniform(-1, 1, size=(size, 2))