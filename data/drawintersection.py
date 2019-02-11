import pygame as pg

from data.abstract.intersectionpoint import IntersectionPoint
from data.utilities.drawhelper import mix_colors


class CircleIntersectionSprite(IntersectionPoint):
    def __init__(self, circle_x, circle_y, update_circles=False):
        super().__init__(circle_x, circle_y, update_circles)      
        self.line_color = mix_colors(circle_x.line_color, circle_y.line_color)
        self.point_color = pg.Color("tomato")
        self.point_radius = 3
