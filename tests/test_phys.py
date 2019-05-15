import pytest
from dexter.phys import Vec2, Box

class TestVec2(object):

    def test_init(self):
        #no args
        v0 = Vec2()
        assert (v0.x, v0.y) == (0, 0)

        #standard constructor
        v1 = Vec2(1, 2)
        assert (v1.x, v1.y) == (1, 2)

    def test_operators(self):
        v0 = Vec2()
        vpos = Vec2(2, 5)
        vneg = Vec2(-2, -5)

        #check eq operator
        assert vpos != vneg
        assert vneg == (-2, -5)
        assert v0 != (0, 1)

        #check the copy operators
        assert (vpos + vneg) == v0
        assert not (v0 is (0, 0)) #are we actually copying?

        #TODO: more tests


class TestBox(object):
    def test_constructor(self):
        box = Box(Vec2(1, 2), 32, 64)
        assert box.pos == (1, 2)
        assert box.width == 32
        assert box.height == 64

        box2 = Box(Vec2())
        assert box2.width == 1
        assert box2.height == 1

    def test_collision(self):
        box = Box(Vec2(), 64, 64)
        box2 = Box(Vec2(64, 64), 64, 64)
        box3 = Box(Vec2(0, 64), 64, 64)
        box4 = Box(Vec2(64, 0), 64, 64)
        assert box.touches(box2)
        assert box2.touches(box)
        assert box.touches(box3)
        assert box3.touches(box)
        assert box.touches(box4)
        assert box4.touches(box)

        