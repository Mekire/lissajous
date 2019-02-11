import pygame as pg

from data.abstract.circlepoint import RotatingPoint


class CirclePointSprite(RotatingPoint):
    def __init__(self, center, radius, seconds_per_rotation, line_color):
        super().__init__(center, radius, seconds_per_rotation)
        self.line_color = pg.Color(line_color)
        self.point_color = pg.Color("tomato")
        self.point_radius = 3
