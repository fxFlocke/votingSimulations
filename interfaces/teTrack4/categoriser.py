import array

NftCategoryIdentifiers = [
    'POK','POE','POC','POA','POE','POC','POC','POE','POA','POC','POK','POK','POK','POK','POK'
]

categoryIndices = [
[0, 10, 11, 12, 13, 14], #POK
[1, 4, 7], #POE
[2, 5, 6, 9], #POC
[3, 8] #POA
]

categoryLabels = [
    "POK",
    "POE",
    "POC",
    "POA"
]

def groupCategories(nftData: array) -> array:
    categories = []
    for i in range(len(categoryIndices)):
        proofCategory = combineCategories(nftData, i)
        categories.append(proofCategory)
    return categories

def combineCategories(nftData: array, categoryIndex) -> array:
    voterCount = len(nftData[0])
    results = [0] * voterCount
    for i in range(voterCount):
        for _, index in enumerate(categoryIndices[categoryIndex]):
            results[i] += nftData[index][i]
    return results