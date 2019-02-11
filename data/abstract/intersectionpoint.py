import pygame as pg

from data.abstract.point import Point


class IntersectionPoint(Point):
    def __init__(self, circle_x, circle_y, update_circles=False):
        self.circles = circle_x, circle_y
        super().__init__((circle_x.pos[0], circle_y.pos[1]))
        self.update_circles = update_circles

    def update(self, dt):
        if self.update_circles:
            for circle in self.circles:
                circle.update(dt)
        self.previous_pos = self.pos
        self.pos = self.circles[0].pos[0], self.circles[1].pos[1]
