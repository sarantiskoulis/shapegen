import argparse
from shape import Scene
import os
import sys
class Run(Scene):
    def __init__(self,args):
        self.args = args
        self._action()

    def _action(self):
        if self.args.delete:
            self.delete_file()

        if self.args.draw and self.args.shape:
            self._draw_in_cli()

        if self.args.shape and self.args.path:
            self.create_file()



    def _draw_in_cli(self):
        print('You have selected a:', Scene(self.args.shape).shape)
        print(Scene(self.args.shape).shape.draw())


    def create_file(self):
        # If path does not exist - create path file
        if not os.path.exists(self.args.path):
            with open(self.args.path, 'w') as f:
                print(f"File created at {self.args.path}")
                f.write(Scene(self.args.shape).shape.draw())

        else:
            print(f"File at {self.args.path} already exists")


    def delete_file(self):
        os.remove(self.args.delete)

class MyNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)