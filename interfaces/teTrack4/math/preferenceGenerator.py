import array
import json
from mechanisms.helpers import createRandomWeights

#groups at index 1, 2, 4, 9, have a preferenceDescription of [0, 0, 1, 0]
description = [[[1, 2, 4, 9], [0, 0, 1, 0]], [[3, 5, 10], [0.7, 0.2, 0.1, 0.0]]]

class PreferenceGenerator:
    """
    This class 
    """
    def __init__(
        self,
        candidatesCount: int,
        voterGroupCount: int,
        preferenceDescription: array
    ) -> None:
        self.candidatesCount = candidatesCount
        self.voterGroupCount = voterGroupCount
        self.preferenceDescription = preferenceDescription
        self.preferences = []
        calculatePreferences(self)

def calculatePreferences(self):
    availableGroups = [0] * self.voterGroupCount
    preference = [0] * self.candidatesCount
    for _ in range(self.voterGroupCount):
        self.preferences.append(preference)
    for _, elem in enumerate(self.preferenceDescription):
        for _, groupIndex in enumerate((elem[0])):
            self.preferences[groupIndex] = elem[1]
            availableGroups[groupIndex] = 1
    for _, groupIndex in enumerate(availableGroups):
        if availableGroups[groupIndex] == 0:
            self.preferences[groupIndex] = createRandomWeights(count=self.candidatesCount)
        
def updateDescription(self, description: array, voterGroupCount: int, candidatesCount: int=0):
    if candidatesCount != 0:
        self.candidatesCount = candidatesCount
    self.voterGroupCount = voterGroupCount
    self.preferenceDescription = description
    calculatePreferences(self)

def generatePreferenceDescription(filePath: str='') -> array:
    if filePath == '':
        filePath = 'interfaces/teTrack4/data/groupedPreferences.json'
    f = open(filePath)
    data = json.load(f)
    preferences = data['preferences']
    return preferences

