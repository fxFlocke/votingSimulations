from interfaces.teTrack4 import transformer
from interfaces.teTrack4 import preferenceGenerator as pg
from votingMechanism import VotingMechanism
from simulation import VotingSimulation
from mechanisms import singleWinnerQCV as swQCV
from mechanisms import rankNslide as rNs

filePath = 'interfaces/teTrack4/data/assumptions/equalDistribution.json'
trackData = transformer.DataToVoterGroupsAndWeights()
preferenceDescription = pg.generatePreferenceDescription(filePath)

def BaseTest():
    mechanism = VotingMechanism(
        votingCreditAllocationFunction=rNs.RankNslideMechanism.votingCreditAllocationFunction,
        voteAccountingFunction=rNs.RankNslideMechanism.voteAccountingFunction,
        socialChoiceFunction=swQCV.SingleWinnerQcvMechanism.socialChoiceFunction
    )
    preferenceGenerator = pg.PreferenceGenerator(
        candidatesCount=4,
        voterGroupCount=len(trackData['voterGroups']),
        preferenceDescription=preferenceDescription
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
    simulation.simulate()