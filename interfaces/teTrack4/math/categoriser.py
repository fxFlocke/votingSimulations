import array

def generateIndices() -> array:
    poks = [i for i in range(0, 9)]
    poks += [20, 19]
    poks += ([i for i in range(22, 31)])
    poes = [10, 14, 16]
    poes += ([i for i in range(32, 41)])
    pocs = ([i for i in range(11, 13)])
    pocs.append(18)
    poas = [15, 17, 21]
    return [poks, poes, pocs, poas]

categoryIndices = generateIndices()
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