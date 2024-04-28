
from simulation import Simulation
from data import *

# scrapeNBAOdds()

algorithm_files = ["team2_algorithm.py"]

simulation_file = "test_sim.xlsx"

# Create a Simulation object
s = Simulation(algorithm_files, simulation_file)

# Run the algorithms to generate bets
bets = s.runAlgos()
for team, bet_list in bets:
    print(f"Team: {team}")
    for bet in bet_list:
        print(bet)