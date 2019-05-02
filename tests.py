import unittest
from dexter.vec2 import Vec2


class TestVec2(unittest.TestCase):

    def setUp(self):
        self.vzero = Vec2()
        self.vpositive = Vec2(100, 50)
        self.vnegative = Vec2(-100, -50)

    def testConstructor(self):
        self.assertEqual(self.vzero.x, 0)
        self.assertEqual(self.vzero.y, 0)
        self.assertEqual(self.vpositive.x, 100)
        self.assertEqual(self.vpositive.y, 50)




unittest.main()
