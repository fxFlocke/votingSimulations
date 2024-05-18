import array
class SingleWinnerQcvMechanism:
    def socialChoiceFunction(grant: float, voteAccounts: array) -> array:
        highestVoteCountIndex = 0
        highestVoteCountValue = 0
        for accID, accountVotes in enumerate(voteAccounts):
            if accountVotes > highestVoteCountValue:
                highestVoteCountValue = accountVotes
                highestVoteCountIndex = accID
        for accID, _ in enumerate(voteAccounts):
            if accID == highestVoteCountIndex:
                voteAccounts[accID] = grant
            else:
                voteAccounts[accID] = 0
        return voteAccounts