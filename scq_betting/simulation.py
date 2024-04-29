# simulation.py

import os
import pandas as pd
from bet import Bet
from datetime import datetime



class Simulation:
    def __init__(self, algorithm_files, simulation_file, max_wager):
        self.algorithm_files = algorithm_files
        self.simulation_file = simulation_file  
        self.max_wager = max_wager
        if not os.path.exists(simulation_file):
            self.initializeSimulationFile()


    def initializeSimulationFile(self):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')

        # Create a writer object
        with pd.ExcelWriter(self.simulation_file) as writer:
            # Iterate over algorithm files to extract team names
            for algo_file in self.algorithm_files:
                team_name = os.path.splitext(os.path.basename(algo_file))[0].split('_')[0]
                # Create a DataFrame for the team with date and balance columns
                team_df = pd.DataFrame(columns=['Date', 'Balance'])
                team_df.loc[0] = [today_date, 100]  # Set initial balance to 100
                # Write the team DataFrame to the Excel file with the team name as the sheet name
                team_df.to_excel(writer, sheet_name=team_name, index=False)

        print(f"Simulation file '{self.simulation_file}' initialized successfully.")

    def isValidBet(self, b):
        if b.wager > self.max_wager:
            print("Invalid wager:", b)
            return False
        
        today_date = datetime.today().strftime('%Y-%m-%d')
        data_file = f"../__data__/betting_data_{today_date}.xlsx"

        try:
            df = pd.read_excel(data_file)
            todays_teams = pd.concat([df["Team 1"], df["Team 2"]])
            
            if b.team not in todays_teams.values:
                print("Invalid team:", b)
                return False

        except FileNotFoundError:
            print("Data file containing today's games not found")
            return False

        return True

    def runAlgos(self):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')
        # File name for storing bets
        bets_file_name = f"../__data__/bets_{today_date}.xlsx"

        # Iterate through algorithm files, create objects, and store list of bets
        for algo_file in self.algorithm_files:
            final_bets = []
            # Extract team name from file name
            team_name = os.path.splitext(os.path.basename(algo_file))[
                0].split('_')[0]
            # Import algorithm class and create object
            algo_module = __import__(algo_file.replace('.py', ''))
            algo_class = getattr(algo_module, 'Algorithm')
            algo_object = algo_class()
            # Call run function and store bets
            bets = algo_object.run()
            valid_bets = []
            for bet in bets:
                if self.isValidBet(bet):
                    valid_bets.append(bet)
                else:
                    print("Invaild Bet:", bet)

            final_bets.append((team_name, valid_bets))

        try:
            with pd.ExcelWriter(bets_file_name) as writer:
                if final_bets:  # Check if valid_bets is not empty
                    for team_name, bets in final_bets:
                        df = pd.DataFrame([vars(bet) for bet in bets])
                        df.to_excel(writer, sheet_name=team_name, index=False)
                else:
                    print("No valid bets to write to Excel.")

        except IndexError as e:
            print("An error occurred while writing to Excel:", e)

        print(f"All valid bets stored in {bets_file_name}")
        return final_bets
        

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
