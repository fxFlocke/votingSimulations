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

    WeightDescription can be used as follows: [0.8, 0.1, 0.1]
    Which distributes the weight of 0.8 to the first Group & so on...

    PreferenceDescription can be used as follows: [[0.2, 0.5, ...], [], [], []]
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
            weightDescription: array=None,
            preferenceDescription: array=None
    ) -> None:
        self.grant = grant
        self.votersCount = votersCount
        self.voters = [0] * votersCount
        self.candidatesCount = candidatesCount
        self.candidates = [0] * candidatesCount
        self.mechanism = mechanism
        self.voterGroups = voterGroups
        self.candidateGroups = candidateGroups
        self.weightDescription = weightDescription
        self.preferenceDescription = preferenceDescription

    def assignVotingCredits(self):
        if self.weightDescription == None:
            self.weightDistribution = helpers.createRandomWeights(False, self.votersCount)
        else:
            self.weightDistribution = helpers.createWeightFromDescription(self.votersCount, self.voterGroups, self.weightDescription)
        self.voters = self.mechanism.votingCreditAllocationFunction(self.grant, self.weightDistribution)

    def vote(self):
        if self.preferenceDescription == None:
            self.preferenceDistribution = helpers.createRandomPreferences(dirichlet=False, votersCount=self.votersCount, candidatesCount=self.candidatesCount)
        else:
            self.preferenceDistribution = helpers.createPreferencesFromDescription(votersCount=self.votersCount, candidatesCount=self.candidatesCount, groups=self.voterGroups, preferenceDescription=self.preferenceDescription)
        self.candidates = self.mechanism.voteAccountingFunction(self.voters, self.preferenceDistribution, self.candidates)

    def choose(self):
        self.candidates = self.mechanism.socialChoiceFunction(self.grant, self.candidates)

    def simulate(self):
        self.assignVotingCredits()
        visualizer.visualizeVotingWeights(self.weightDistribution, self.votersCount)
        visualizer.visualizeVoterCredits(self.voters, self.votersCount)
        self.vote()
        visualizer.visualizeCandidateVotes(self.candidates, self.candidatesCount)
        self.choose()
        visualizer.visualizeGrantDistribution(self.candidates, self.candidatesCount)

    