import pygame as pg

from data import constants
from data.drawrotation import CirclePointSprite
from data.drawintersection import CircleIntersectionSprite
from data.utilities.drawhelper import draw_point, draw_path


class App(object):
    def __init__(self):
        self.setup_surfaces()
        self.setup_objects()
        self.clock = pg.time.Clock()
        self.done = False

    def setup_surfaces(self):
        self.screen = pg.display.get_surface()
        self.fader = self.screen.copy().convert_alpha()
        self.fader.fill(constants.FADE_BACK)
        self.temp_surface = self.screen.copy().convert_alpha()
        self.temp_surface.fill(constants.BACKGROUND)

    def setup_objects(self):
        self.circles = self.make_circles()
        self.intersections = self.make_intersections()
        self.all_objects = self.circles + self.intersections

    def make_circles(self):
        circles = []
        base_seconds_per_rotation = constants.PERIOD
        radius, color_names = constants.RADIUS, constants.COLOR_NAMES
        for i in range(0, constants.COLUMNS):
            seconds_per_rotation = base_seconds_per_rotation / (i+1)
            circles.append(CirclePointSprite(((3*radius)+i*(2*radius), radius),
                radius, seconds_per_rotation, color_names[i%len(color_names)]))
            circles.append(CirclePointSprite((radius, (3*radius)+i*(2*radius)),
                radius, seconds_per_rotation, color_names[i%len(color_names)]))
        return circles

    def make_intersections(self):
        intersections = []
        for circ_x in self.circles[0::2]:
            for circ_y in self.circles[1::2]:
                intersections.append(CircleIntersectionSprite(circ_x, circ_y))
        return intersections

    def update(self, dt):
        for obj in self.all_objects:
            obj.update(dt)

    def render(self):
        for obj in self.all_objects:
            draw_path(self.temp_surface, obj)
        self.screen.blit(self.temp_surface, (0,0))
        self.temp_surface.blit(self.fader, (0,0))
        for obj in self.all_objects:
            draw_point(self.screen, obj)
        pg.display.update()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def main_loop(self):
        dt = 0
        while not self.done:
            self.event_loop()
            self.update(dt)
            self.render()
            dt = self.clock.tick(constants.FPS) / 1000.0
