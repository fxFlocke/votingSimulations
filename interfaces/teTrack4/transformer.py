import pandas as pd
from . import patternVisualizer
from . import categoriser
from . import synergyGenerator

# Define the columns to read for the NFT data
columnReadDescriptionNFTdata = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
]
columnReadDescriptionNFTweights = ['Category', 'Weight']

# Amplifiers mapping
amplifiers = {
    'POE': 5,
    'POK': 4,
    'POC': 3,
    'F': 2,
    'POA': 1.5
}

# from, to, strength
synergyStrength = [1, 1, 1, 1, 1, 1]

voterCount = 0
combinedScores = 0

def readNFTdataOfVoters() -> list:
    nftData = []
    for _, columnToRead in enumerate(columnReadDescriptionNFTdata):
        csvValues = pd.read_csv("interfaces/teTrack4/data/nft_data_may_28_2024_cleaned.csv", usecols=[columnToRead], dtype=int)
        convertedValues = csvValues.to_numpy().flatten()
        nftData.append(convertedValues)
    return nftData

def readNFTweights() -> pd.DataFrame:
    csvValues = pd.read_csv("interfaces/teTrack4/data/votingWeightsComm.csv", usecols=columnReadDescriptionNFTweights)
    return csvValues

def calculateVoterScores(voterData: list, weights: pd.DataFrame, amplifiers: dict) -> list:
    # Extract categories and weights
    categories = weights['Category'].tolist()
    raw_weights = weights['Weight'].tolist()
    
    # Apply amplifiers to weights based on categories
    amplified_weights = [raw_weights[i] * amplifiers.get(categories[i], 1) for i in range(len(categories))]

    # Extract Categories
    categoryResults = categoriser.groupCategories(voterData)

    # Extract Synergies
    synergyResults = synergyGenerator.calculateSynergies(voterData)

    # Calculate voter scores
    voterScores = [0] * len(voterData[0])
    for i, voterDataSet in enumerate(voterData):
        for j, nftValue in enumerate(voterDataSet):
            voterScores[j] += nftValue * amplified_weights[i]
            for _, synergy in enumerate(synergyResults):
                voterScores[j] += synergy[j]
            for _, category in enumerate(categoryResults):
                voterScores[j] += category[j] 
    return voterScores

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
    return groupIndicators    

def transformGroupsToSimulationInput(groupIndicator: list) -> dict:
    global combinedScores
    global voterCount
    groupAmount = len(groupIndicator)
    voterGroups = [0] * groupAmount
    weights = [0] * groupAmount
    for i, indicator in enumerate(groupIndicator):
        voterGroups[i] = indicator[0] / voterCount
        weights[i] = (indicator[0] * indicator[1]) / combinedScores
    results = {
        'voterCount': voterCount,
        'voterGroups': voterGroups,
        'weights': weights
    }
    return results

def DataToVoterGroupsAndWeights() -> dict:
    nftData = readNFTdataOfVoters()
    #patternVisualizer.visualizeRelations(nftData)
    nftWeights = readNFTweights()
    voterScores = calculateVoterScores(nftData, nftWeights, amplifiers)
    voterScores.sort()
    groupIndicators = formGroups(voterScores)
    transformedData = transformGroupsToSimulationInput(groupIndicators)
    return transformedData

