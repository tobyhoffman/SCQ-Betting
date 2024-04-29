from simulation import Simulation
from data import *

# scrapeNBAOdds()

algorithm_files = ["team2_algorithm.py"]

simulation_file = "../__data__/test_sim.xlsx"

# Create a Simulation object
s = Simulation(algorithm_files, simulation_file, 10)

# Run the algorithms to generate bets
bets = s.runAlgos()
if(bets):
    for team, bet_list in bets:
        print(f"Team: {team}")
        for bet in bet_list:
            print(bet)

else:
    print("No bets placed")
