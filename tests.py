from votingMechanism import VotingMechanism
from simulation import VotingSimulation
import array

# social choice function from Track 4 to plug in
def socialChoiceFunction(grant: float, voteAccounts: array) -> array:
    highestVoteCountIndex = 0
    highestVoteCountValue = 0
    for accID, accountVotes in enumerate(voteAccounts):
        if accountVotes > highestVoteCountValue:
            highestVoteCountValue = accountVotes
            highestVoteCountIndex = accID
    for accID, _ in enumerate(voteAccounts):
        if accID == highestVoteCountIndex:
            voteAccounts[accID] = grant
        else:
            voteAccounts[accID] = 0
    return voteAccounts

#just a few examples

def randomTest():
    mechanism = VotingMechanism()
    simulation = VotingSimulation(
        grant=10000,
        votersCount=20,
        candidatesCount=4,
        mechanism=mechanism,
    )
    simulation.simulate()

def equalDistributionTest():
    mechanism = VotingMechanism()
    simulation = VotingSimulation(
        grant=10000,
        votersCount=20,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=[0.25, 0.25, 0.25, 0.25],
        weightDescription=[0.5, 0.5, 0, 0],
        preferenceDescription=[[0.5, 0, 0, 0.5], [0, 0.5, 0.5, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    )
    simulation.simulate()

def lowParticipationTest():
    mechanism = VotingMechanism()
    simulation = VotingSimulation(
        grant=10000,
        votersCount=20,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=[0.5, 0.5],
        weightDescription=[0.5, 0.5],
        preferenceDescription=[[0.5, 0.5, 0, 0], [0, 0, 0, 0]]
    )
    simulation.simulate()

def highWeightConcentrationTest():
    mechanism = VotingMechanism(
        socialChoiceFunction=socialChoiceFunction
    )
    simulation = VotingSimulation(
        grant=10000,
        votersCount=10,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=[0.2, 0.3, 0.4, 0.1],
        weightDescription=[0.1, 0.1, 0.1, 0.7],
        preferenceDescription=[[0.2, 0.6, 0.2, 0], [0.3, 0.5, 0.2, 0], [0.1, 0.5, 0.4, 0], [0, 0, 0, 1]]
    )
    simulation.simulate()