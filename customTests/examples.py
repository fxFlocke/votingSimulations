from votingMechanism import VotingMechanism
from simulation import VotingSimulation
from mechanisms import singleWinnerQCV as swQCV
from mechanisms import rankNslide as rNs
from mechanisms import groupHug as gH
from mechanisms import helpers

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
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=rNs.RankNslideMechanism.voteAccountingFunction,
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
        votingCreditAllocationFunction=rNs.RankNslideMechanismMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=rNs.WeightedClusteringMechanism.voteAccountingFunction
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
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=gH.GroupHugMechanism.voteAccountingFunction,
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

def RankQCVTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
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

def QCVDictatorTest():
    mechanism = VotingMechanism(
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    voterCount = 200
    divisors=[20, 120, 39, 20, 1]
    voterGroups=helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
    simulation = VotingSimulation(
        grant=10000,
        votersCount=voterCount,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=voterGroups,
        weightDescription=[0, 0.005, 0.005, 0.00, 0.99],
        preferenceDescription=[[0, 0, 0, 0], [0, 0.8, 0.2, 0], [0.2, 0.6, 0.2, 0], [0.33, 0.33, 0.33, 0], [0, 0, 0, 1]]
    )
    for i in range(0, int(voterCount/len(divisors)-1)):
        for j in range(len(divisors)-1):
            voterCount-=1
            divisors[j] -= 1
            voterGroups = helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
            winner=simulation.simulate(visuals=False)
            if winner==3:
                print('dictator for voterCount: ', voterCount)

def RankNSlideDictatorTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    voterCount = 200
    divisors=[20, 120, 39, 20, 1]
    voterGroups=helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
    simulation = VotingSimulation(
        grant=10000,
        votersCount=voterCount,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=voterGroups,
        weightDescription=[0, 0.005, 0.005, 0.00, 0.99],
        preferenceDescription=[[0, 0, 0, 0], [0, 0.8, 0.2, 0], [0.2, 0.6, 0.2, 0], [0.33, 0.33, 0.33, 0], [0, 0, 0, 1]]
    )
    for i in range(0, int(voterCount/len(divisors)-1)):
        for j in range(len(divisors)-1):
            voterCount-=1
            divisors[j] -= 1
            voterGroups = helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
            winner=simulation.simulate(visuals=False)
            if winner==3:
                print('dictator for voterCount: ', voterCount)

def GroupHugDictatorTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=gH.GroupHugMechanism.voteAccountingFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    voterCount = 200
    divisors=[20, 120, 39, 20, 1]
    voterGroups=helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
    simulation = VotingSimulation(
        grant=10000,
        votersCount=voterCount,
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=voterGroups,
        weightDescription=[0, 0.005, 0.005, 0.00, 0.99],
        preferenceDescription=[[0, 0, 0, 0], [0, 0.8, 0.2, 0], [0.2, 0.6, 0.2, 0], [0.33, 0.33, 0.33, 0], [0, 0, 0, 1]]
    )
    for i in range(0, int(voterCount/len(divisors)-1)):
        for j in range(len(divisors)-1):
            voterCount-=1
            divisors[j] -= 1
            voterGroups = helpers.generateVoterGroups(divisors=divisors,voterCount=voterCount)
            winner=simulation.simulate(visuals=False)
            if winner==3:
                print('dictator for voterCount: ', voterCount)
