from interfaces.teTrack4 import transformer
from interfaces.teTrack4.math import preferenceGenerator as pg
from votingMechanism import VotingMechanism
from simulation import VotingSimulation
from mechanisms import singleWinnerQCV as swQCV
from mechanisms import rankNslide as rNs

trackData = transformer.DataToVoterGroupsAndWeights()

def BaseTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=rNs.RankNslideMechanism.voteAccountingFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    preferenceGenerator = pg.PreferenceGenerator(
        candidatesCount=4,
        voterGroupCount=len(trackData['voterGroups']),
        preferenceDescription=trackData['preferences']
    )
    simulation = VotingSimulation(
        grant=10000,
        votersCount=trackData['voterCount'],
        candidatesCount=4,
        mechanism=mechanism,
        voterGroups=trackData['voterGroups'],
        weightDescription=trackData['weights'],
        preferenceDescription=preferenceGenerator.preferences
    )
    simulation.simulate(visuals=True)


def parameterFinding():
    ""