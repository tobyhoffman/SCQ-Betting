from data import *
from simulation import Simulation

algorithm_files = ["team1_algorithm.py",
                   "team2_algorithm.py", "team3_algorithm.py"]

simulation_file = "test_sim.xlsx"

today_date = datetime.today().strftime("%Y-%m-%d")
# getResults('2024-04-29')

scrapeNBAOdds()