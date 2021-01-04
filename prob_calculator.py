import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

        self.copied_list = copy.copy(self.contents)

    def add_balls_back(self, dict1):
        for k, v in dict1.items():
            for _ in range(v):
                self.contents.append(k)
        

    def draw(self, number_to_draw):
        draw_list = []        
        if number_to_draw > len(self.contents):
            return self.contents
        
        for _ in range(number_to_draw):
            random_int = random.randint(0, len(self.contents)-1)
            draw_list.append(self.contents[random_int])
            self.contents.pop(random_int)

        return draw_list



            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    check = 0
    copied_list = copy.deepcopy(hat.contents)[:]
    for _ in range(num_experiments):
        random_balls = hat.draw(num_balls_drawn)
        dict_random_balls = dict(Counter(random_balls))
        for k, v in expected_balls.items():
            try:
                if dict_random_balls[k] >= v:
                    check += 1
            except:
                check += 0

        if check == len(expected_balls):
            counter += 1
        
        check = 0
        hat.contents = []
        for i in copied_list:
            hat.contents.append(i)

    probability = counter/num_experiments
    return probability