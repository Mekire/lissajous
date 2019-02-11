class Point(object):
    def __init__(self, position):
        self.pos = position
        self.previous_pos = self.pos

    def point_as_integer(self, x, y):
        return int(x), int(y)

    @property
    def int_pos(self):
        return self.point_as_integer(*self.pos)

    @property
    def int_previous_pos(self):
        return self.point_as_integer(*self.previous_pos)
