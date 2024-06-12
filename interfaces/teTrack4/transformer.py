import pandas as pd
from . import patternVisualizer
from .math import categoriser
from .math import synergyGenerator
from .web import extractor
import array

# Define the columns to read for the NFT data
columnReadDescriptionNFTdata = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
]
columnReadDescriptionNFTweights = ['Category', 'Weight']

# Amplifiers mapping
amplifiers = {
    'proof of expertise': 1,
    'proof of knowledge': 17,
    'proof of contribution': 1,
    'proof of attendance': 1
}

# from, to, strength
synergyStrength = [
    1,
    10,
    10,
    1,
    1,
    1,
    1,
    1,
    1,
    1
]

voterCount = 0
combinedScores = 0

# def readNFTdataOfVoters() -> list:
#     nftData = []
#     for _, columnToRead in enumerate(columnReadDescriptionNFTdata):
#         csvValues = pd.read_csv("interfaces/teTrack4/data/nft_data_may_28_2024_cleaned.csv", usecols=[columnToRead], dtype=int)
#         convertedValues = csvValues.to_numpy().flatten()
#         nftData.append(convertedValues)
#     return nftData

def readNFTweights() -> pd.DataFrame:
    csvValues = pd.read_csv("interfaces/teTrack4/data/votingWeightsComm.csv", usecols=columnReadDescriptionNFTweights)
    return csvValues

def smoothScores(scores: array) -> array:
    wholeScore = 0
    newScores = [0] * len(scores)
    for _, score in enumerate(scores):
        wholeScore += score
    for i, score in enumerate(scores):
        #adjust when someone has to be smoothed out
        #cap that more people fit in the expert description
        if (score/wholeScore) > 0.0055:
            newScores[i] = wholeScore * 0.0055
        else:
            newScores[i] = score
    return newScores

def calculateVoterScores(voterData: list, weights: pd.DataFrame, amplifiers: dict) -> list:
    # Extract categories and weights
    categories = weights['Category'].tolist()
    raw_weights = weights['Weight'].tolist()
    
    # Apply amplifiers to weights based on categories
    amplified_weights = [raw_weights[i] * amplifiers.get(categories[i], 1) for i in range(len(categories))]

    # Extract Categories
    categoryResults = categoriser.groupCategories(voterData)
    # Extract Synergies
    #combinedData = extractor.getCombinedCategories()
    synergyResults = synergyGenerator.calculateSynergies(categoryResults)

    # Calculate voter scores
    voterScores = [0] * len(voterData[0])
    for i, voterDataSet in enumerate(voterData):
        for j, nftValue in enumerate(voterDataSet):
            voterScores[j] += nftValue * amplified_weights[i]
            for i, synergy in enumerate(synergyResults):
                voterScores[j] += nftValue * (synergy[j] * synergyStrength[i])
    smoothedScores = smoothScores(voterScores)
    return smoothedScores

def formGroups(scores: list) -> list:
    global voterCount
    global combinedScores
    groupIndicators = []
    voterCount = len(scores)
    combinedScores = 0
    groupAmount = 0
    for i, score in enumerate(scores):
        combinedScores += score
        groupAmount += 1
        if i == voterCount - 1 or scores[i + 1] != score:
            groupIndicators.append([groupAmount, score])
            groupAmount = 0
    print(groupIndicators)
    return groupIndicators   

def generatePreferences(groupIndicators: list) -> array:
    preferences = []
    wholeScores = 0
    for _, indicator in enumerate(groupIndicators):
        wholeScores += (indicator[0] * indicator[1])
    expertShare = 0
    expertIndices = []
    outIndex = 0
    expertCount = 0
    for i in range((len(groupIndicators)-1), 0, -1):
        #adjust how much the expert group is(significantly smaller than the others)
        #adjust how much smaller the expert group is
        if expertShare > 0.29:
            outIndex = i
            break
        expertCount += groupIndicators[i][0]
        expertShare += (groupIndicators[i][0] * groupIndicators[i][1]) / wholeScores
        print(expertCount, "   :", str(expertShare))
        expertIndices.append(i)

    expertPreferenceDescription = [expertIndices, [0, 0, 0, 1]]
    nonExpertIndices = [i for i in range(0,outIndex)]
    nonExpertPreferenceDescription = [nonExpertIndices, [1, 0, 0, 0]]
    preferences.append(expertPreferenceDescription)
    preferences.append(nonExpertPreferenceDescription)
    return preferences

def transformGroupsToSimulationInput(groupIndicators: list) -> dict:
    global combinedScores
    global voterCount
    groupAmount = len(groupIndicators)
    voterGroups = [0] * groupAmount
    weights = [0] * groupAmount
    for i, indicator in enumerate(groupIndicators):
        voterGroups[i] = indicator[0] / voterCount
        weights[i] = (indicator[0] * indicator[1]) / combinedScores
    preferences = generatePreferences(groupIndicators)
    print(preferences)
    results = {
        'voterCount': voterCount,
        'voterGroups': voterGroups,
        'weights': weights,
        'preferences': preferences
    }
    return results

def DataToVoterGroupsAndWeights() -> dict:
    nftData = extractor.extractNFTdata()
    #patternVisualizer.visualizeRelations(nftData)
    nftWeights = readNFTweights()
    voterScores = calculateVoterScores(nftData, nftWeights, amplifiers)
    voterScores.sort()
    groupIndicators = formGroups(voterScores)
    transformedData = transformGroupsToSimulationInput(groupIndicators)
    return transformedData