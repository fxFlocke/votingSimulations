from votingMechanism import VotingMechanism
import mechanisms.helpers as helpers
import visualizer
import array

class VotingSimulation:
    """
    This Simulation takes a Voting Mechanism & different Configurations as Input,
    Mechanism, Grant and Voterscount are self explanatory.

    If you are using random values & set this value to true, 
    the voters are making a single choice, instead of a distribution of credits.
    Otherwise you can describe this with the preferencDescription.

    VoterGroups can be used as follows: [0.2, 0.2, 0.6]
    Which Groups 20%, 20% and 60% of the Voters

    Same for the Candidate Groups

    WeightRange can be used as follows: [1, 2, 'int']
    The first two Elements are giving the lower & uppper bound.
    The third element lets you decide to allow only integers or floats between these ranges
    !!Range without description generates random values & then calculates the weight for each voter
    !!Range combined with description assigns the values inside the description to the voter groups &
    !!Then calculates the weights based on this

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
            singlePreference: bool=False,
            voterGroups: array=None,
            candidateGroups: array=None,
            weightRange: array=None,
            weightDescription: array=None,
            preferenceDescription: array=None
    ) -> None:
        self.grant = grant
        self.votersCount = votersCount
        self.voters = [0] * votersCount
        self.candidatesCount = candidatesCount
        self.candidates = [0] * candidatesCount
        self.mechanism = mechanism
        self.singlePreference=singlePreference
        self.voterGroups = voterGroups
        self.candidateGroups = candidateGroups
        self.weightRange = weightRange
        self.weightDescription = weightDescription
        self.preferenceDescription = preferenceDescription
        self.winner=0

    def assignVotingCredits(self):
        if self.weightDescription == None:
            if self.weightRange == None:
                self.weightDistribution = helpers.createRandomWeights(self.votersCount)
            else:
                self.weightDistribution = helpers.createRandomWeightsFromRange(self.votersCount, self.weightRange)
        else:
            if self.weightRange == None:
                self.weightDistribution = helpers.createWeightFromDescription(self.votersCount, self.voterGroups, self.weightDescription)
            else:
                self.weightDistribution = helpers.createWeightFromDescriptionAndRange(self.votersCount, self.voterGroups, self.weightDescription)
        self.voters = self.mechanism.votingCreditAllocationFunction(self.grant, self.weightDistribution)

    def vote(self):
        if self.preferenceDescription == None:
            if self.singlePreference == True:
                self.preferenceDistribution = helpers.createSingleRandomizedPreferences(votersCount=self.votersCount, candidatesCount=self.candidatesCount)
            else:
                self.preferenceDistribution = helpers.createMultiRandomizedPreferences(votersCount=self.votersCount, candidatesCount=self.candidatesCount)
        else:
            self.preferenceDistribution = helpers.createPreferencesFromDescription(votersCount=self.votersCount, candidatesCount=self.candidatesCount, groups=self.voterGroups, preferenceDescription=self.preferenceDescription)
        self.candidates = self.mechanism.voteAccountingFunction(self.voters, self.preferenceDistribution, self.candidates)

    def choose(self) -> int:
        [self.candidates,self.winner]  = self.mechanism.socialChoiceFunction(self.grant, self.candidates)

    def simulate(self, visuals: bool=True) -> int:
        self.assignVotingCredits()
        if visuals:
            visualizer.visualizeVotingWeights(self.weightDistribution, self.votersCount)
            visualizer.visualizeVoterCredits(self.voters, self.votersCount)
        self.vote()
        if visuals:
            visualizer.visualizeCandidateVotes(self.candidates, self.candidatesCount)
        self.choose()
        if visuals:
            visualizer.visualizeGrantDistribution(self.candidates, self.candidatesCount)
        return self.winner