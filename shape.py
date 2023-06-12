class Scene:
    def __init__(self, object):
        self.obj = object.lower()
        self.shape_dict = {
            'cube':Cube(),
            'line':Line(),
            'trig':Trig()
        }
        self.shape = self.shape_dict[self.obj]


class Cube():
    def __init__(self):
        self.name = 'cube'
    def __repr__(self):
        return self.name
    def draw(self):
        return '|---|\n|   |\n|___|'

class Line():
    def __init__(self):
        self.name = 'line'
    def __repr__(self):
        return self.name
    def draw(self):
        return " __________  "

class Trig():
    def __init__(self):
        self.name = 'trig'
    def __repr__(self):
        return self.name
    def draw(self):
        return "   /\ \n  /  \ \n /    \ \n ------"