import array
import math

class VotingMechanism:
    """
    This Mechanism-Template implements the Quadratic-Credibility-Voting-Mechanism
    You are able to write your own functions, that can be passed for the instantiation, 
    to run simulations with your own Voting-Mechanism.

    The Functions are structured as follows:

    votingCreditAllocationFunction(grant: float, weights: array[float]) -> int
        Based on the weights and the Grant, this function assigns Voting-Tokens that
        be used by the voters. If you want to give every Voter one Token, just allocate 
        an array with the size of the weights, where each element is a '1' and return it.

    voteAccountingFunction(votedTokens: int) -> int
        Here, you can apply specific rules, how the voted-tokens are accounted.
        By default this method uses Quadratic-Funding & Quadrativ-Voting to improve Incentive-Compatability.

    socialChoiceFunction(grant: float, voteAccounts: array[float]) -> array[float]
        This function chooses how the Grant will be distributed between candidates. 
        By default this Method distributes the Grant based on total shares to the candidates. 
        If you just want to reward the winner, you can use the function provided in singleWinnerQCV.py
    """

    def votingCreditAllocationFunction(grant: float, weights: array) -> array:
        summedWeights = 0
        for weight in weights:
            summedWeights += weight
        voterCredits = [0] * len(weights)
        for wID, weight in enumerate(weights):
            voterCredits[wID] = grant * (weight / summedWeights)
        return voterCredits

    def voteAccountingFunction(voters: array, preferences: array, candidates: array) -> array:
        for vID, voterPrefs in enumerate(preferences):
            for cID, _ in enumerate(candidates):
                # qudratic funding rule
                candidates[cID] += math.sqrt(float(voterPrefs[cID] * voters[vID]))
        for cID, _ in enumerate(candidates):
            # quadratic voting rule
            candidates[cID] = math.pow(candidates[cID], 2)
        return candidates

    def socialChoiceFunction(grant: float, voteAccounts: array) -> array:
        summedVotes = 0 
        for accountVotes in voteAccounts:
            summedVotes += accountVotes
        for accID, account in enumerate(voteAccounts):
            voteAccounts[accID] = grant * (account / summedVotes)
        return voteAccounts

    def __init__(
            self,
            votingCreditAllocationFunction=votingCreditAllocationFunction,
            voteAccountingFunction=voteAccountingFunction,
            socialChoiceFunction=socialChoiceFunction
    ) -> None:
        self.votingCreditAllocationFunction = votingCreditAllocationFunction
        self.voteAccountingFunction = voteAccountingFunction
        self.socialChoiceFunction = socialChoiceFunction