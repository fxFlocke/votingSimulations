import math
import array
import random as ran

def createRandomWeights(count: int) -> array:
    weights = [0] * count
    sum = 0
    for i in range(count):
        r = ran.random()
        sum += r
        weights[i] = r
    for wID in range(count):
        weights[wID] /= sum
    return weights

def createRandomChoice(count: int) -> array:
    voterPreference = [0] * count
    candidateChoice = ran.choice([i for i in range [count]])
    voterPreference[candidateChoice] = 1

def createWeightFromDescription(count: int, groups: array, weightDescription: array) -> array:
    weights = [0] * count
    offset = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * count)):
            weights[i] = (weightDescription[gID] / (groupSize * count))
        offset += floorOrCeil(groupSize * count)
    print(weights)
    return weights
    
def createRandomWeightsFromRange(count: int, weightRange: array) -> array:
    weights = [0] * count
    sum = 0
    if weightRange[2] == "int":
        for i in range(count):
            weights[i] = ran.randint(weightRange[0], weightRange[1])
            sum += weights[i]
    if weightRange[2] == "float":
        for i in range(count):
            weights[i] = ran.randint(weightRange[0], weightRange[1])
            sum += weights[i]
    print(weights)
    for wID in range(count):
        weights[wID] /= sum
    print(weights)
    return weights    
    
def createWeightFromDescriptionAndRange(count: int, groups: array, weightDescription: array) -> array:
    weights = [0] * count
    offset = 0
    sum = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * count)):
            weights[i] = weightDescription[gID]
            sum += weights[i]
        offset += floorOrCeil(groupSize * count)
    for wID in range(count):
        weights[wID] /= sum
    return weights    

def createMultiRandomizedPreferences(votersCount: int, candidatesCount: int) -> array:
    preferences = [[0] * candidatesCount for i in range(votersCount)] 
    for i in range(0, votersCount):
        preferences[i] = createRandomWeights(count=candidatesCount) 
    return preferences

def createSingleRandomizedPreferences(votersCount: int, candidatesCount: int) -> array:
    preferences = [[0] * candidatesCount for i in range(votersCount)] 
    for i in range(0, votersCount):
        preferences[i] = createRandomChoice(candidatesCount)
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