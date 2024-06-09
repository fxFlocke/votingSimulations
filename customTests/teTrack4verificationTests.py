from interfaces.teTrack4 import transformer

trackData = transformer.DataToVoterGroupsAndWeights()

def BaseTest():
    print(trackData['voterCount'])
    print(trackData['voterGroups'])
    print(trackData['weights'])