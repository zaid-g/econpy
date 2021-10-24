import random
import math
import numpy as np


def sample_item_from_dictionary(dict_):
    rand_val = random.random()
    total = 0
    for k, v in dict_.items():
        total += v
        if rand_val <= total:
            return k
    assert False, "unreachable"


class Poisson:
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    def sample(self):
        return np.random.poisson(self.lambda_)

    def sample_discrete(self):
        return math.floor(np.random.poisson(self.lambda_))
