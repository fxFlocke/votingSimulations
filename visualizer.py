import array
import matplotlib.pyplot as plt

def visualizeVotingWeights(weights: array, votersCount: int):
    voters = [i for i in range(votersCount)]
    plt.plot(voters, weights, 'o')
    plt.xlabel("Voters")
    plt.ylabel("Weights")
    plt.show()

def visualizeVoterCredits(voterAccounts: array, votersCount: int): 
    voters = [i for i in range(votersCount)]
    plt.plot(voters, voterAccounts, 'o')
    plt.xlabel("Voters")
    plt.ylabel("Credits")
    plt.show()

def visualizeCandidateVotes(candidateAccounts: array, candidatesCount: int):
    candidates = [i for i in range(candidatesCount)]
    plt.plot(candidates, candidateAccounts, 'o')
    plt.xlabel("Candidates")
    plt.ylabel("Votes")
    plt.show()

def visualizeGrantDistribution(candidateAccounts: array, candidatesCount):
    candidates = [i for i in range(candidatesCount)]
    plt.plot(candidates, candidateAccounts, 'o')
    plt.xlabel("Candidates")
    plt.ylabel("Grant")
    plt.show()