
import array

# Define Weights for the Voters clustered here
ClusterStrengths = [0.2, 0.4, 0.6, 0.8]

class GroupHugMechanism:
    def voteAccountingFunction(voters: array, preferences: array, candidates: array) -> array:
        global ClusterStrengths
        # adjust clusterCounts in respect to the amount of Strengths here
        clusters = clusterVoterByWeights(voters, 4)
        candidatesCount = len(candidates)
        finalCandidateVotes = [0] * candidatesCount
        for clusterID, cluster in enumerate(clusters):
             clusterVotes = getClusterVotes(cluster, voters, preferences, candidatesCount)
             for candidateID, candidateVotes in enumerate(clusterVotes):
                  finalCandidateVotes[candidateID] = candidateVotes * ClusterStrengths[clusterID]
        return finalCandidateVotes

def getClusterVotes(cluster: array, voters: array, preferences: array, candidatesCount: int) -> array:
     clusterPreference = [0] * candidatesCount
     for voter in cluster:
          for cID in range(candidatesCount):
               clusterPreference[cID] += (preferences[voter][cID] * voters[voter])
     return clusterPreference

def clusterVoterByWeights(weights: array, clusterCount: int) -> array:
        maxValue = getMaxValue(weights)
        tresholds = createTresholds(clusterCount, maxValue)
        global Clusters
        clusters =  [[] for i in range(clusterCount)] 
        tID = clusterCount - 1
        for wID, weight in enumerate(weights):
            for _ in range(clusterCount):
                 if weight >= tresholds[tID]:
                      clusters[tID].append(wID)
                      break
                 tID -= 1
            tID = clusterCount - 1
        return clusters

def createTresholds(clusterCount: int, maxValue) -> array:
        tresholdSubtractor = maxValue / clusterCount 
        treshold = maxValue
        tresholds = [0] * clusterCount
        for i in range(clusterCount):
            tresholds[i] = treshold
            treshold -= tresholdSubtractor
        return tresholds    

def getMaxValue(weights: array) -> array:
     max = 0
     for weight in weights:
          if weight > max:
               max = weight
     return max