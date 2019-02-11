import pygame as pg

from copy import deepcopy


FPS = 60
SCREEN_SIZE = (640, 640)

BACKGROUND = pg.Color("black")
FADE_BACK = deepcopy(BACKGROUND)
FADE_BACK.a = 5

RADIUS = 40
COLUMNS = (SCREEN_SIZE[0] // (2*RADIUS)) - 1
PERIOD = 2

COLOR_NAMES = ("red", "orange", "yellow", "green",
               "lightblue", "violet", "purple")
