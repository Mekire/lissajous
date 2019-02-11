import pygame as pg


def draw_point(surface, obj):
    pg.draw.circle(surface, obj.point_color, obj.int_pos, obj.point_radius)


def draw_path(surface, obj, width=1):
    pg.draw.line(surface, obj.line_color, obj.int_previous_pos,
                 obj.int_pos, width)


def mix_colors(one, two):
    add = [a+b for a,b in zip(one, two)]
    return [color // 2 for color in add[:3]] 
