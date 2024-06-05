import math
import array
import random as ran

LastSum = 0

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
    candidateChoice = ran.choice([i for i in range(count)])
    voterPreference[candidateChoice] = 1
    return voterPreference

def createWeightFromDescription(count: int, groups: array, weightDescription: array) -> array:
    weights = [0] * count
    offset = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * count)):
            weights[i] = (weightDescription[gID] / (groupSize * count))
        offset += floorOrCeil(groupSize * count)
    return weights
    
def createRandomWeightsFromRange(count: int, weightRange: array) -> array:
    weights = [0] * count
    global LastSum
    LastSum = 0
    if weightRange[2] == "int":
        for i in range(count):
            weights[i] = ran.randint(weightRange[0], weightRange[1])
            LastSum += weights[i]
    if weightRange[2] == "float":
        for i in range(count):
            weights[i] = ran.randint(weightRange[0], weightRange[1])
            LastSum += weights[i]
    for wID in range(count):
        weights[wID] /= LastSum
    return weights    

def translateWeightsToValues(weights: array) -> array:
    global LastSum
    for wID in range(len(weights)):
        weights[wID] *= LastSum
    return weights  
    
def createWeightFromDescriptionAndRange(count: int, groups: array, weightDescription: array) -> array:
    weights = [0] * count
    offset = 0
    global LastSum
    LastSum = 0
    for gID, groupSize in enumerate(groups):
        for i in range(offset, offset + floorOrCeil(groupSize * count)):
            weights[i] = weightDescription[gID]
            LastSum += weights[i]
        offset += floorOrCeil(groupSize * count)
    for wID in range(count):
        weights[wID] /= LastSum
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
    
def generateVoterGroups(divisors: array, voterCount: int) -> array:
    voterGroups = [0] * len(divisors)
    for i in range(len(divisors)):
        voterGroups[i] = (divisors[i] / voterCount)
    return voterGroups