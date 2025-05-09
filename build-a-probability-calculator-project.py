import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for i in kwargs.items():
            for n in range(i[1]):
                self.contents.append(i[0])

    def draw(self, number_drawn):
        drawn = []
        minim = min(number_drawn, len(self.contents))
    
        for n in range(minim):
            drawn.append(self.contents.pop(random.randrange(len(self.contents))))
        return drawn

    def __str__(self):
        return str(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    
    for i in range(num_experiments):
        HAT = copy.deepcopy(hat)
        drawn = HAT.draw(num_balls_drawn)
    
        drawn_dict = {}
        for ball in expected_balls:
            drawn_dict[f'{ball}'] = 0
            
        for ball in drawn:
            if ball not in drawn_dict:
                drawn_dict[f'{ball}'] = 1
            else:
                drawn_dict[f'{ball}'] += 1

        m = 0
        for exp in expected_balls:
            if drawn_dict[exp] >= expected_balls[exp]:
                m += 1

        if m == len(expected_balls):
            M += 1

    probability = M/num_experiments

    return probability

hat1 = Hat(red=4, green= 2, blue =4)
#print(hat1)
#print(hat1.draw(3))

N = 10
print(experiment(Hat(black=6, red=4, green=3), {'red':2, 'green':1}, 5, N))
