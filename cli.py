import argparse
from shape import Scene
class Run(Scene):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--shape', type=str, required=True)
        self.parser.add_argument('--draw', type=str)
        self.args = self.parser.parse_args()
        self.statement()


    def statement(self):
        if self.args.draw:
            print(Scene(self.args.shape).shape.draw())
        else:
            print('You have selected a:', Scene(self.args.shape).shape)