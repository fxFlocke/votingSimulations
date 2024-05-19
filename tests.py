from votingMechanism import VotingMechanism
from simulation import VotingSimulation
from mechanisms import singleWinnerQCV as swQCV
from mechanisms import rangedVoting as rV
from mechanisms import weightedClustering as wC
import array

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
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
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

def singleRandomizedPreferenceTest():
    mechanism = VotingMechanism()
    simulation = VotingSimulation(
        grant=10000,
        votersCount=10,
        candidatesCount=4,
        mechanism=mechanism,
        singlePreference=True,
        voterGroups=[0.2, 0.3, 0.4, 0.1],
        weightRange=[1, 5, "int"],
    )
    simulation.simulate()

def multiRandomizedPreferenceTets():
    mechanism = VotingMechanism()
    simulation = VotingSimulation(
        grant=10000,
        votersCount=10,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=[0.2, 0.3, 0.4, 0.1],
        weightRange=[1, 12, "int"],
    )
    simulation.simulate()

def weightedVotingTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rV.RangedVotingMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=rV.RangedVotingMechanism.voteAccountingFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    simulation = VotingSimulation(
        grant=10000,
        votersCount=100,
        candidatesCount=4,
        mechanism=mechanism,
        singlePreference=True,
        voterGroups=[0.2, 0.3, 0.4, 0.1],
        weightRange=[1, 2, "int"],
        weightDescription=[1, 1, 2, 2],
        preferenceDescription=[[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    simulation.simulate()

def randomCusteringTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rV.RangedVotingMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=wC.WeightedClusteringMechanism.voteAccountingFunction
    )
    simulation = VotingSimulation(
        grant=10000,
        votersCount=20,
        candidatesCount=4,
        mechanism=mechanism,
        singlePreference=True,
    )
    simulation.simulate()

def describedClusteringTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rV.RangedVotingMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=wC.WeightedClusteringMechanism.voteAccountingFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    simulation = VotingSimulation(
        grant=10000,
        votersCount=100,
        candidatesCount=4,
        mechanism=mechanism,
        singlePreference=True,
        voterGroups=[0.2, 0.3, 0.4, 0.1],
        weightRange=[1, 12, "int"],
        weightDescription=[4, 7, 9, 11],
        preferenceDescription=[[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    simulation.simulate()

def rangedQCVTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rV.RangedVotingMechanism.votingCreditAllocationFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
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