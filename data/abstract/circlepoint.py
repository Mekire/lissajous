import math

from data.abstract.point import Point


TWO_PI = 2 * math.pi


class RotatingPoint(Point):
    def __init__(self, center, radius, seconds_per_rotation):
        super().__init__((center[0] + radius, center[1]))
        self.center = center
        self.radius = radius
        self.angular_speed = (TWO_PI) / seconds_per_rotation
        self.angle = 0

    def update(self, dt):
        self.previous_pos = self.pos
        self.angle += self.angular_speed * dt
        self.angle %= TWO_PI
        x = self.center[0] + self.radius * math.cos(self.angle)
        y = self.center[1] + self.radius *  math.sin(self.angle)
        self.pos = x, y
