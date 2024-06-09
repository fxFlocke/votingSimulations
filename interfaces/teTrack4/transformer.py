import array
import pandas as p

columnReadDescriptionNFTdata =  [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
]
columnReadDescriptionNFTweights = 4
voterCount = 0
combinedScores = 0

def readNFTdataOfVoters() -> array:
    nftData = []
    for _, columnToRead in enumerate(columnReadDescriptionNFTdata):
        csvValues = p.read_csv("interfaces/teTrack4/data/nft_data_may_28_2024_cleaned.csv", usecols=[columnToRead], dtype=int)
        convertedValues = csvValues.to_numpy().flatten()
        nftData.append(convertedValues)
    return nftData

def readNFTweights() -> array:
    csvValues = p.read_csv("interfaces/teTrack4/data/votingWeights.csv", usecols=[columnReadDescriptionNFTweights], dtype=int)
    return csvValues.to_numpy().flatten()

def calculateVoterScores(voterData: array, weights: array) -> array:
    voterScores = [0] * len(voterData[0])
    for i, voterDataSet in enumerate(voterData):
        for j, nftValue in enumerate(voterDataSet):
            voterScores[j] += nftValue * weights[i]
    return voterScores

def formGroups(scores: array) -> array:
    groupIndicators = []
    global voterCount
    voterCount = len(scores)
    global combinedScores
    groupAmount = 0
    for i, score in enumerate(scores):
        combinedScores += score
        groupAmount += 1
        if(i == voterCount-1):
            groupIndicators.append([groupAmount, score])
            groupAmount = 0
            break
        if(scores[i+1] != score):
            groupIndicators.append([groupAmount, score])
            groupAmount = 0
    return groupIndicators    

def transformGroupsToSimulationInput(groupIndicator: array) -> array:
    global combinedScores
    global voterCount
    groupAmount = len(groupIndicator)
    voterGroups = [0] * groupAmount
    weights = [0] * groupAmount
    for i, indicator in enumerate(groupIndicator):
        voterGroups[i] = indicator[0] / voterCount
        weights[i] = (indicator[0] * indicator[1]) / combinedScores
    results = dict()
    results['voterCount'] = voterCount
    results['voterGroups'] = voterGroups
    results['weights'] = weights
    return results

def DataToVoterGroupsAndWeights() -> dict:
    transformedData = dict()
    nftData = readNFTdataOfVoters()
    nftWeights = readNFTweights()
    voterScores = calculateVoterScores(nftData,nftWeights)
    voterScores.sort()
    groupIndicators = formGroups(voterScores)
    transformedData = transformGroupsToSimulationInput(groupIndicators)
    return transformedData