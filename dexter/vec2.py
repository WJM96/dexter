import math


class Vec2(object):
    """docstring for Vec2."""

    __slots__ = [
        "x", "y"
    ]

    def __init__(self, x=0, y=0):
        super(Vec2, self).__init__()
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x * self.x) + (self.y * self.y)

    def magnitudeSqr(self):
        return (self.x * self.x) + (self.y * self.y)

    def getNormalized(self, arg):
        len = self.magnitude()
        if len != 0:
            return Vec2(
                self.x/len,
                self.y/len)
        else:
            return Vec2()

    # Operators

    def __add__(self, rhs):
        return Vec2(
            self.x + rhs.x,
            self.y + rhs.y)

    def __iadd__(self, rhs):
        self.x += rhs.x
        self.y += rhs.y

    def __sub__(self, rhs):
        return Vec2(
            self.x - rhs.x,
            self.y - rhs.y)

    def __isub__(self, rhs):
        self.x -= rhs.x
        self.y -= rhs.y

    def __mul__(self, scalar):
        return Vec2(
            self.x * scalar,
            self.y * scalar)

    def __imul__(self, rhs):
        self.x *= rhs.x
        self.y *= rhs.y

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vec2(
                self.x / scalar,
                self.y / scalar)
        else:
            return Vec2()

    def __itruediv__(self, scalar):
        if scalar != 0:
            self.x /= scalar,
            self.y /= scalar
