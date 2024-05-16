from votingMechanism import VotingMechanism
from simulation import VotingSimulation

mechanism = VotingMechanism()
simulation = VotingSimulation(
    grant=10000,
    votersCount=100,
    candidatesCount=4,
    mechanism=mechanism,
    weightRange=[0,2]
)
simulation.simulate()