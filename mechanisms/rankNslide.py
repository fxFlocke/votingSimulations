import array
from . import helpers

class RankNslideMechanism:
    def votingCreditAllocationFunction(grant: float, weights: array) -> array:
        voterCredits = helpers.translateWeightsToValues(weights)
        return voterCredits

    def voteAccountingFunction(voters: array, preferences: array, candidates: array) -> array:
        for vID, voterPrefs in enumerate(preferences):
            for cID, _ in enumerate(candidates):
                candidates[cID] += voterPrefs[cID] * voters[vID]
        return candidates