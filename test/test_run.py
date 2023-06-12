import unittest
from cli import Run, MyNamespace
import argparse
import os


with open('cube.txt', 'w') as f:
    f.write('Run test delete function file')



class TestRun(unittest.TestCase):
    def test_delete_file(self):

        with open('cube.txt', 'w') as f:
            f.write('Run test delete function file')

        args = MyNamespace(shape=None, path=None, draw=False, delete='cube.txt')
        Run(args)


        filename = 'cube.txt'


        file_exists = os.path.exists(filename)

        self.assertFalse(file_exists)
