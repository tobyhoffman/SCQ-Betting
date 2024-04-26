# simulation.py

import os
import pandas as pd
from bet import Bet
from datetime import datetime


class Simulation:
    def __init__(self, algorithm_files, simulation_file):
        self.algorithm_files = algorithm_files
        self.simulation_file = simulation_file

    def runAlgos(self):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')
        # File name for storing bets
        bets_file_name = f"bets_{today_date}.xlsx"

        # Iterate through algorithm files, create objects, and store list of bets
        all_bets = []
        for algo_file in self.algorithm_files:
            # Extract team name from file name
            team_name = os.path.splitext(os.path.basename(algo_file))[
                0].split('_')[0]
            print(team_name)
            # Import algorithm class and create object
            algo_module = __import__(algo_file.replace('.py', ''))
            algo_class = getattr(algo_module, 'Algorithm')
            algo_object = algo_class()
            # Call run function and store bets
            bets = algo_object.run()
            all_bets.append((team_name, bets))

        with pd.ExcelWriter(bets_file_name) as writer:
            for team_name, bets in all_bets:
                df = pd.DataFrame([vars(bet) for bet in bets])
                df.to_excel(writer, sheet_name=team_name, index=False)

        print(f"All bets stored in {bets_file_name}")
        return all_bets

    def verifyBets(self, max_wager):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')
        # Load bets from the Excel file
        bets_file_name = f"bets_{today_date}.xlsx"
        all_verified_bets = []

        with pd.ExcelFile(bets_file_name) as xls:
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name)
                # Check if the DataFrame contains the necessary columns
                if 'Team 1' in df.columns and 'Team 2' in df.columns and 'Wager' in df.columns:
                    # Filter bets for today's games and with wager no greater than max_wager
                    verified_bets = df[(df['Team 1'] == today_date) | (
                        df['Team 2'] == today_date) & (df['Wager'] <= max_wager)]
                    all_verified_bets.append((sheet_name, verified_bets))
                else:
                    print(
                        f"Columns 'Team 1', 'Team 2', or 'Wager' not found in sheet {sheet_name}. Skipping...")

        return all_verified_bets

    def computeResults(self):
        # Get today's actual results from Excel file
        # Example file name, replace with actual file name
        today_results = pd.read_excel('actual_results.xlsx')

        # Get current balances from simulation file
        simulation_df = pd.read_excel(self.simulation_file)

        # Iterate through each team's bets and compute profit/loss
        for team, bets in self.runAlgos():
            # Compute profit/loss for each bet and update current balance
            for bet in bets:
                # Implement profit/loss calculation based on actual results
                # Example: profit_loss = calculate_profit_loss(bet, today_results)
                # Update current balance in simulation_df
                pass

        # Save updated current balances back to simulation file
        simulation_df.to_excel(self.simulation_file, index=False)
