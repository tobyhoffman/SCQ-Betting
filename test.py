from data import *
from simulation import Simulation

algorithm_files = ["team1_algorithm.py",
                   "team2_algorithm.py", "team3_algorithm.py"]

simulation_file = "test_sim.xlsx"

# Create a Simulation object
s = Simulation(algorithm_files, simulation_file)

# Run the algorithms to generate bets
bets_file = s.runAlgos()

# Verify and filter bets for today's games and with a max wager of 10 units
verified_bets = s.verifyBets(max_wager=10)

# Print verified bets for each team
for team_name, bets in verified_bets:
    print(f"Verified bets for {team_name}:")
    print(bets)


