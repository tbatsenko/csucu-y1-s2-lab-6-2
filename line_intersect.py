# File: line_intersect.py
# This module allows to check if two lines with given coords intersects.


class Line(object):
    # y = kx + b - line equation
    def __init__(self, coords):
        self.coords = coords
        if coords[0] == coords[1]:
            self.coords = None


    def get_tg(self):
        k = (self.coords[0][1] - self.coords[1][1])/(
            self.coords[0][0] - self.coords[1][0])
        return k

    def get_b(self):
        return self.coords[0][1] - self.get_tg()*self.coords[0][0]

    def intersect(self, line):
        if not self.coords:
            return None
        k1, k2 = self.get_tg(), line.get_tg()
        b1, b2 = self.get_b(), line.get_b()
        if k1 == k2 and b1 == b2:
            return self
        elif k1 == k2:
            return None
        else:
            x = (b2-b1)/(k1-k2)
            y = k1*x + b1
            return x, y


def line_intersect(line1, line2):
    return line1.intersect(line2)
