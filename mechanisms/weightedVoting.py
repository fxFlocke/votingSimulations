import array
import math

class WeightedVoting:
    def votingCreditAllocationFunction(grant: float, weights: array) -> array:
        voterCredits = [0] * len(weights)
        for wID, weight in enumerate(weights):
            voterCredits[wID] = grant * weight
        return voterCredits

    def voteAccountingFunction(voters: array, preferences: array, candidates: array) -> array:
        for vID, voterPrefs in enumerate(preferences):
            for cID, _ in enumerate(candidates):
                candidates[cID] += float(voterPrefs[cID] * voters[vID])
        for cID, _ in enumerate(candidates):
            # quadratic voting rule
            candidates[cID] = math.pow(candidates[cID], 2)
        return candidates
