import array
from  . import deserializer

def generateIdentifiers() -> array:
    identifiers = ["POK"] * 10
    identifiers.append("POE")
    identifiers += ["POC"] * 3
    identifiers += ["POE", "POA"] * 2
    identifiers.append("POC")
    identifiers += ["POK"] * 2
    identifiers.append("POA")
    identifiers += ["POK"] * 8
    identifiers += ["POE"] * 12
    identifiers.append("POA")
    identifiers.append("POC")
    return identifiers

def generateRawVoterData(voterCount) -> array:
    voters = [[0] * voterCount for i in range(10)]
    voters.append([0] * voterCount)
    voters += [[0] * voterCount for i in range(3)]
    voters += [[0] * voterCount for i in range(2)]
    voters.append([0] * voterCount)
    voters += [[0] * voterCount for i in range(2)]
    voters.append([0] * voterCount)
    voters += [[0] * voterCount for i in range(8)]
    voters += [[0] * voterCount for i in range(12)]
    voters.append([0] * voterCount)
    voters.append([0] * voterCount)
    return voters

nftGroupIdentifiers = generateIdentifiers()
combinedCategories = []
rawVoterData = []
POKs = []
POEs = []
POCs = []
POAs = []

def appendPOK(tokenID, voterID):
    global POKs
    if nftGroupIdentifiers[tokenID] == "POK":
        POKs[voterID] += 1

def appendPOE(tokenID, voterID):
    global POEs
    if nftGroupIdentifiers[tokenID] == "POE":
        POEs[voterID] += 1

def appendPOC(tokenID, voterID):
    global POCs
    if nftGroupIdentifiers[tokenID] == "POC":
        POCs[voterID] += 1

def appendPOA(tokenID, voterID):
    global POAs
    if nftGroupIdentifiers[tokenID] == "POA":
        POAs[voterID] += 1

def createCategories(voterCount: int) -> array:
    global POKs
    global POEs
    global POCs
    global POAs
    POKs = [0] * voterCount
    POEs = [0] * voterCount
    POCs = [0] * voterCount
    POAs = [0] * voterCount

def appendForAccount(account: deserializer.Account, voterID):
    global rawVoterData
    for _, token in enumerate(account.tokens.items):
        appendPOK(int(token.tokenId), voterID)
        appendPOE(int(token.tokenId), voterID)
        appendPOC(int(token.tokenId), voterID)
        appendPOA(int(token.tokenId), voterID)
        for i in range(len(rawVoterData)):
            if int(token.tokenId)-1 == i:
                rawVoterData[i][voterID] = 1

def combineCategories() -> array:
    global POKs
    global POEs
    global POCs
    global POAs
    combinedCategories = [POKs,  POEs,  POCs,  POAs]
    return combinedCategories

def extractNFTdata() -> array:
    global nftGroupIdentifiers
    global combinedCategories
    global rawVoterData
    indexedNfts = deserializer.deserializeData()
    rawVoterData = generateRawVoterData(len(indexedNfts.data.accounts.items))
    createCategories(len(indexedNfts.data.accounts.items))
    for i, account in enumerate(indexedNfts.data.accounts.items):
        appendForAccount(account, i)
    combinedCategories = combineCategories()
    return rawVoterData

def getCombinedCategories() -> array:
    global combinedCategories
    return combinedCategories