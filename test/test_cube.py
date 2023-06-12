import unittest
from shape import Cube

class TestCube(unittest.TestCase):
    def test_add(self):
        cube = Cube()
        cube_draw = cube.draw()

        cube_drawing = '|---|\n|   |\n|___|'
        self.assertEqual(cube_draw, cube_drawing)





