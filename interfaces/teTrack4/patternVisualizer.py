import array
import matplotlib.pyplot as plt
from .math import synergyGenerator
from .math import categoriser

colors = [plt.cm.RdBu_r(i/5) for i in range(10)]

def visualizeRelations(nftData: array):
    yAxis = [i for i in range(len(nftData[0]))]
    categories = categoriser.groupCategories(nftData)
    for i, category in enumerate(categories):
        plt.plot(category, yAxis, color=colors[i], label=categoriser.categoryLabels[i])
    plt.legend()
    plt.show()
    synergyResults = synergyGenerator.calculateSynergies(categories,visuals=True)
    for i, synergy in enumerate(synergyResults):
        plt.plot(synergy, yAxis, 'o', color=colors[i], label=synergyGenerator.synergyLabels[i][1])
    plt.legend()
    plt.show()

