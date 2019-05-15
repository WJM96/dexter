import math


class Vec2(object):
    """2D Vector class with math + utility functions."""

    __slots__ = [
        "x", "y"
    ]

    def __init__(self, x: float = 0, y: float = 0):
        super(Vec2, self).__init__()
        self.x = x
        self.y = y
    
    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x) + (self.y * self.y)

    def magnitudeSqr(self) -> float:
        return (self.x * self.x) + (self.y * self.y)

    def getNormalized(self, arg) -> 'Vec2':
        len = self.magnitude()
        if len != 0:
            return Vec2(
                self.x/len,
                self.y/len)
        else:
            return Vec2()

    # Operators

    def __eq__(self, other) -> bool:
        if hasattr(other, "x") and hasattr(other, "y") and other.x == self.x and other.y == self.y:
            return True
        elif isinstance(other, tuple) and other[0] == self.x and other[1] == self.y:
            return True
        else:
            return False
    
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
