import pygame
import numpy as np
import itertools

from car import Car
from dna import DNA
from rpy_reader import Rpy_Utils
from population import Population

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Deep Racer Evo Sim v1")






clock = pygame.time.Clock()
fps = 15


dna = DNA(10)

population = []



map = Rpy_Utils("Cosmic_Loop", screen_height, screen_width, 40)

center_tuple = []
borders = []

for arr in map.center_line:
    center_tuple.append((arr[0], arr[1]))
border_1 = []
for arr in map.inner_border:
    border_1.append((arr[0], arr[1]))
border_2 = []
for arr in map.outer_border:
    border_2.append((arr[0], arr[1]))

borders.append(border_1)
borders.append(border_2)


borders_arr = []
borders_arr.append(map.outer_border)
borders_arr.append(map.inner_border)



reward_dots = map.center_line[::10]


GENERATION = 0
POPULATION_SIZE = 20
STEPS = len(map.center_line)*10
CURR_STEP = 0

START_X = map.center_line[0][0]
START_Y = map.center_line[0][1]


population = Population(POPULATION_SIZE, START_X, START_Y, STEPS, reward_dots=reward_dots)

def detect_colision(curr, next_, p):
    d1 = np.linalg.norm(curr-p)
    d2 = np.linalg.norm(next_-p)
    len = np.linalg.norm(curr-next_)
    buffer = 0.1


    if (d1+d2 >= len-buffer and d1+d2 <= len+buffer) :
        return True
    return False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

   
    
    screen.fill((255, 255, 255))
    # DRAW MAP
    pygame.draw.lines(screen, (0,0,199), True, center_tuple, width=1)
    pygame.draw.lines(screen, (0,0,230), True, border_1, width=2)
    pygame.draw.lines(screen, (0,0,230), True, border_2, width=2)

    # RUN Population 
    for car in population.cars:
        car.run_instr(screen, CURR_STEP)
        if not car.is_crashed:
            for border in borders_arr:
                    for i in range(len(border)-1):
                        curr, next_ = border[i], border[i+1]
                        colided = detect_colision(curr, next_, car.pos)
                        if colided:
                            car.crash_it()
    
    # DRAW REWARD DOTS
    for dot in reward_dots:
        pygame.draw.circle(screen, (0,255,0), (dot[0], dot[1]), 5)
    
    pygame.display.flip()


    clock.tick(60)
    CURR_STEP = CURR_STEP + 1

    if CURR_STEP == STEPS:
        # Cambio de generación
        GENERATION += 1
        CURR_STEP = 0
        population.evaluate()
            


pygame.quit()