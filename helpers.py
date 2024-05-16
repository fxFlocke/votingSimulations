import math
import array
import random as ran
import numpy as np

def floorOrCeilCredits(quadraticVotes: float) -> int:
    subtractor = math.floor(quadraticVotes)
    if (quadraticVotes - subtractor) < 0.5:
        return int(math.floor(quadraticVotes))
    else:
        return int(math.ceil(quadraticVotes))

def createRandomWeights(dirichlet: bool, count: int, weightRange: array) -> array:
    if dirichlet:
        return np.random.dirichlet(np.ones(count), size=1)
    else:
        weights = [0] * count
        s = 0
        for i in range(len(weights)):
            r = ran.random()
            s += r
            weights[i] = r
        for wID in range(len(weights)):
            weights[wID] /= s
        return weights