from votingMechanism import VotingMechanism
import helpers
import visualizer
import array

class VotingSimulation:
    """
    This Simulation takes a Voting Mechanism & different Configurations as Input,
    Mechanism, Grant and Voterscount are self explanatory.

    VoterGroups can be used as follows: [0.2, 0.2, 0.6]
    Which Groups 20%, 20% and 60% of the Voters

    Same for the Candidate Groups

    WeightDistribution can be used as follows: [1, 1.5, 0.5]
    Which assign a weight of 1 to the first Group & so on...

    PreferenceDistribution can be used as follows: [[0.2, 0.5, ...], [], [], []]
    Each Array represents the preference of a Voter-Group
    0.2 indicates that these VotingGroup distribute 20% of their Voting-Power to the first candidate & so on... 
    """

    def __init__(
            self,
            grant: float,
            votersCount: int,
            candidatesCount: int,
            mechanism: VotingMechanism,
            voterGroups: array=None,
            candidateGroups: array=None,
            weightRange: array=[0,1],
            weightDistribution: array=None,
            preferenceDistribution: array=None
    ) -> None:
        self.grant = grant
        self.votersCount = votersCount
        self.voters = [0] * votersCount
        self.candidatesCount = candidatesCount
        self.candidates = [0] * candidatesCount
        self.mechanism = mechanism
        self.voterGroups = voterGroups
        self.candidateGroups = candidateGroups
        self.weightRange = weightRange
        self.weightDistribution = weightDistribution
        self.preferenceDistribution = preferenceDistribution

    def assignVotingCredits(self):
        if self.weightDistribution == None:
            self.weightDistribution = helpers.createRandomWeights(False, self.votersCount, self.weightRange)
        self.voters = self.mechanism.votingCreditAllocationFunction(self.grant, self.weightDistribution)

    def vote(self):
        ""

    def choose(self):
        ""

    def simulate(self):
        self.assignVotingCredits()
        visualizer.visualizeVotingWeights(self.weightDistribution, self.votersCount)

    