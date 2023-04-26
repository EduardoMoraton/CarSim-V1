import numpy as np
import os

class Rpy_Utils:
    def __init__(self, map_name, h, w, scale):
        (self.center_line, self.inner_border, self.outer_border) = self.load_map(map_name)
        self.center_line *= scale
        self.inner_border *= scale
        self.outer_border *= scale
        self.w = w
        self.h = h
        for a in (self.center_line, self.inner_border, self.outer_border):
            self.apply_center(a)

    def load_map(self, map_name):
        waypoints = np.load("./tracks/%s" % map_name + ".npy")

        center_line = waypoints[:,0:2]
        inner_border = waypoints[:,2:4]
        outer_border = waypoints[:,4:6]
        return(center_line, inner_border, outer_border)
    
    def apply_center(self, act):
        for i in range(len(act)):
            curr = act[i]
            curr[0] += self.w/2
            curr[1] += self.h/2
            act[i] = curr
