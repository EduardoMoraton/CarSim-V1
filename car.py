import pygame
import numpy as np

from dna import DNA

class Car:
    fitness = 0
    curr_dot = 0

    def __init__(self, pos, dna_size, reward_dots):
        self.pos = np.array(pos, dtype=float)
        self.size = (5, 5)
        self.color = (np.random.randint(low=0, high=256), np.random.randint(low=0, high=256), np.random.randint(low=0, high=256)) 
        self.velocity = np.zeros(2) 
        self.dna = DNA(dna_size)
        self.is_crashed = False
        self.reward_dots = reward_dots
    

    def draw(self, screen):
        rect = pygame.Rect(*self.pos, *self.size)
        pygame.draw.rect(screen, self.color, rect)

    def update(self, force):
        if not self.is_crashed:
            acceleration = force / self.size 
            self.velocity += acceleration
            self.pos += self.velocity

    def crash_it(self):
        self.velocity = np.zeros(2)
        self.is_crashed = True
    
    def run_instr(self, screen, i):
        self.update(self.dna.instr[i])
        self.draw(screen)

    def reset(self, pos):
        self.pos = np.array(pos, dtype=float)
        self.velocity = np.zeros(2)
        self.is_crashed = False

    def calc_fitness(self):
        dot = self.reward_dots[self.curr_dot]
        dist = np.linalg.norm(self.pos-dot)
        if dist < 0.5:
            self.curr_dot += 1
        self.fitness = dist + self.curr_dot