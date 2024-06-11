import array
import matplotlib.pyplot as plt

colors = [plt.cm.RdBu_r(i/5) for i in range(10)]
synergies = [
    [0,1],
    [0,2],
    [0,3],
    [1,2],
    [1,3],
    [2,3],
    [0,1,2],
    [0,1,3],
    [1,2,3],
    [0,1,2,3]
]
synergyLabels = [
    ["Voters", "POK&POE"],
    ["Voters", "POK&POC"],
    ["Voters", "POK&POA"],
    ["Voters", "POE&POC"],
    ["Voters", "POE&POA"],
    ["Voters", "POC&POA"],
    ["Voters", "POK&POE&POC"],
    ["Voters", "POK&POE&POA"],
    ["Voters", "POE&POC&POA"],
    ["Voters", "All"]
]


def calculateSynergies(combinedData: array, visuals: bool=False) -> array:
    voterCount = len(combinedData[0])
    yAxis = [i for i in range(voterCount)]
    synergyResults = []
    for i, synergy in enumerate(synergies):
        synergyResult = [0] * voterCount
        for j in range(voterCount):
            for _, nftDatasetIndex in enumerate(synergy):
                if combinedData[nftDatasetIndex][j] != 0:
                    synergyResult[j] += combinedData[nftDatasetIndex][j]
                else:
                    synergyResult[j] = 0
                    break
        synergyResults.append(synergyResult)
        if visuals:
            plt.plot(synergyResult, yAxis, 'o', color=colors[i])
            plt.ylabel(synergyLabels[i][0])
            plt.xlabel(synergyLabels[i][1])
            plt.show()
    return synergyResults

#The synergies should go stronger in the following order

#weak
#POA with POK
#POC with POK

#middle
#POA with POC
#POE with POC
#POE with POA

#strong
#POE with POC with POA