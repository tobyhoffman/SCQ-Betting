from simulation import Simulation

algorithm_files = ["team1_algorithm.py"]

simulation_file = "test_sim.xlsx"

# Create a Simulation object
s = Simulation(algorithm_files, simulation_file)

# Run the algorithms to generate bets
bets = s.runAlgos()