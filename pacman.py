import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.SysFont('calibri', 20)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

WHITE = (255, 255, 255)
RED = (248,143,147)
GREEN = (186,217,181)
FONT = (66,12,20)
BACK = (239,247,207)

BLOCK_SIZE = 20
SPEED = 15

class Pacman: