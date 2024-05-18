import array
import matplotlib.pyplot as plt
import numpy as np

def visualizeVotingWeights(weights: array, votersCount: int):
    voters = np.arange(1, votersCount + 1)
    plt.plot(voters, weights, 'o')
    plt.xlabel("Voters")
    plt.xticks(range(1, votersCount + 1))
    plt.ylabel("Weights")
    plt.show()

def visualizeVoterCredits(voterAccounts: array, votersCount: int): 
    voters = np.arange(1, votersCount + 1)
    plt.plot(voters, voterAccounts, 'o')
    plt.xlabel("Voters")
    plt.xticks(range(1, votersCount + 1))
    plt.ylabel("Credits")
    plt.show()

def visualizeCandidateVotes(candidateAccounts: array, candidatesCount: int):
    candidates = np.arange(1, candidatesCount + 1)
    plt.plot(candidates, candidateAccounts, 'o')
    plt.xlabel("Candidates")
    plt.xticks(range(1, candidatesCount + 1))
    plt.ylabel("Votes")
    plt.show()

def visualizeGrantDistribution(candidateAccounts: array, candidatesCount):
    candidates = np.arange(1, candidatesCount + 1)
    plt.plot(candidates, candidateAccounts, 'o')
    plt.xlabel("Candidates")
    plt.xticks(range(1, candidatesCount + 1))
    plt.ylabel("Grant")
    plt.show()