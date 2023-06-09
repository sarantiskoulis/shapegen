import argparse
from shape import Scene
import os
import sys
class Run(Scene):
    def __init__(self):
        self._cli_init()


    def _draw_in_cli(self):
        if self.args.shape:
            print('You have selected a:', Scene(self.args.shape).shape)
            print(Scene(self.args.shape).shape.draw())

    def _cli_init(self):
        self.parser = argparse.ArgumentParser(description='Create a new file at the specified path')
        self.parser.add_argument('--shape', type=str)
        self.parser.add_argument('--path', type=str, help='Path of the new file to create')
        self.parser.add_argument('--draw', type=str, help='Draw object into file')
        self.parser.add_argument('--delete', type=str, help='Delete file')
        self.args = self.parser.parse_args()

        self.create_file()

        if self.args.delete:
            self.delete_file()
    def create_file(self):
        if self.args.path:
            if not os.path.exists(self.args.path):
                with open(self.args.path, 'w') as f:
                    print(f"File created at {self.args.path}")
                    if self.args.shape:
                        f.write(Scene(self.args.shape).shape.draw())
            else:
                print(f"File already exists at {self.args.path}")
        else:
            self._draw_in_cli()

    def delete_file(self):
        os.remove(self.args.delete)

