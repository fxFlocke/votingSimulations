import math
import array
import random as ran
import numpy as np

def createRandomWeights(dirichlet: bool, count: int) -> array:
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

def createWeightFromDescription(count: int, groups: array, weightDescription: array) -> array:
    weights = [0] * count
    offset = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * count)):
            weights[i] = (weightDescription[gID] / (groupSize * count))
        offset += floorOrCeil(groupSize * count)
    return weights

def createRandomPreferences(dirichlet: bool, votersCount: int, candidatesCount: int) -> array:
    preferences = [[0] * candidatesCount for i in range(votersCount)] 
    for i in range(0, votersCount):
        preferences[i] = createRandomWeights(dirichlet=dirichlet, count=candidatesCount) 
    return preferences

def createPreferencesFromDescription(votersCount: int, candidatesCount: int, groups: array, preferenceDescription: array) -> array:
    preferences = [[0] * candidatesCount for i in range(votersCount)]
    offset = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * votersCount)):
            preferences[i] = preferenceDescription[gID]
        offset += floorOrCeil(groupSize * votersCount)
    return preferences

def voteRandomized(voters: array, candidates: array, accountingFunc) -> array:
    for voter in voters:
        for i in voter:
            candidates[ran.randint(0, len(candidates))] += accountingFunc(1)
    return candidates

def floorOrCeil(val: float) -> int:
    subtractor = math.floor(val)
    if (val - subtractor) < 0.5:
        return int(math.floor(val))
    else:
        return int(math.ceil(val))