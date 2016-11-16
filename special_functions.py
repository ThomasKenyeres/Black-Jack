import time

class Animations():
    def __init__(self):
        self.thinking_pics = [
            '   o o   O O   o o   O O   o o   O O',
            '   O O   o o   O O   o o   O O   o o',
            '   0_0   O O   0_0   O O   0_0   O O',
            '   O O   0_0   O O   0_0   O O   0_0'
        ]


    def Loading(self, string):
        for j in range(0, 8):
            for i in range(0, len(self.thinking_pics)):
                t = str(string) + str(self.thinking_pics[i-1])
                print(t, end="\r\r")
                time.sleep(0.1)




Animations = Animations()


Animations.Loading("Thinking")
