import numpy as np
from random import uniform
from math import pi, cos, sin

def table(n: int) -> np.array:
    tab = np.zeros((1, 4))
    for i in range(n):
        X, Y = uniform(0, 800), uniform(0,800)
        theta = uniform(-pi, pi)
        vel = uniform(0, 1)
        r = np.array([X, Y, theta, vel])

        tab = np.vstack((tab, r))

    return tab

def get_color(vel: float) -> tuple:
    return (60, 160, vel*255)

def walk(pos: tuple, theta: float, vel: float) -> (tuple):
    X, Y = pos
    
    dX = vel * cos(theta)
    dY = vel * sin(theta)

    new_pos = (X + dX, Y + dY)
    return new_pos
