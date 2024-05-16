from typing import Optional
from helpers import floorOrCeilCredits
import array
import math

class VotingMechanism:
    """
    This Mechanism-Template implements the Quadratic-Credibility-Voting-Mechanism
    You are able to write your own functions, that can be passed for the instantiation, 
    to run simulations with your own Voting-Mechanism.

    The Functions are structured as follows(description below the function head):

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
        If you just want to reward the winner, assign the Grant to the 1st Element
        in the voteAccounts, 0 to the rest of Elements & return it.
    """

    def votingCreditAllocationFunction(grant: float, weights: array) -> array:
        summedWeights = 0
        for weight in weights:
            summedWeights += weight
        voterCredits = [0] * len(weights)
        for wID, weight in enumerate(weights):
            voterCredits[wID] = grant * (weight / summedWeights)
        return voterCredits

    def voteAccountingFunction(votedTokens: int) -> int:
        # quadratic funding rule
        quadraticFundingVotes = math.sqrt(float(votedTokens))
        smoothedQFvotes = floorOrCeilCredits(quadraticFundingVotes)
        # qudratic voting rule
        return math.pow(smoothedQFvotes, 2)

    def socialChoiceFunction(grant: float, voteAccounts: array) -> array:
        summedVotes = 0 
        for accountVotes in voteAccounts:
            summedVotes += accountVotes
        for accID, account in voteAccounts:
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


