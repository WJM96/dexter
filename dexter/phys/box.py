from .vec2 import Vec2
import pygame


class Box(object):
    """
        2D, axis aligned bounding box.
    """
    __slots__ = [
        "pos", "width", "height"
    ]

    def __init__(self, pos: Vec2, width: float = 1, height: float = 1):
        super(Box, self).__init__()
        self.pos = pos
        self.width = width
        self.height = height

    def touches(self, other) -> bool:
        return not (self.pos.x > other.pos.x + other.width or self.pos.x + self.width < other.pos.x or 
                    self.pos.y > other.pos.y + other.height or self.pos.y + self.height < other.pos.y)

    def debug_draw(self, screen):
        pygame.draw.rect(
            screen, (255, 0, 0), 
            pygame.Rect(self.pos.x, self.pos.y, self.width, self.height), 2)