import array
import matplotlib.pyplot as plt
import numpy as np

def visualizeVotingWeights(weights: array, votersCount: int):
    voters = np.arange(0, votersCount)
    plt.plot(voters, weights)
    plt.xlabel("Voters")
    plt.ylabel("Weights")
    plt.show()

def visualizeCandidateVotes(candidates: array, candidatesCount: int):
    ""

def visualizeGrantDistribution(candidates: array, candidatesCount):
    ""