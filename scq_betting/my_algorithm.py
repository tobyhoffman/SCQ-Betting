from bet import Bet
from data import *
from game import Game
import re
import requests
from bs4 import BeautifulSoup
from gamesplits import GameSplits

class Algorithm:


    def __init__(self):
        # Initialize any parameters or variables needed for your betting strategy
        pass
    @staticmethod
    def divide_chunks(l, n): 
        # looping till length l 
        for i in range(0, len(l), n):  
            yield l[i:i + n]

    def run(self):

        bets = []
# URL of the website with the table
        url = 'https://www.sportsbettingdime.com/nba/public-betting-trends/'

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table on the webpage (you may need to inspect the HTML source to determine the table's class or id)
            table = soup.find()

            if table:
                rows1 = table.find_all('tr')
                raw_data = []
                raw_odds = []
                for row in rows1:
                    # Extract data from each row            
                    datacells = row.find_all('td', class_='odds-cell')
                    cells = row.find_all('td')
                    for cell in cells:
                        # Process or print the cell data
                        #if(cell.text[0].isdigit()):
                        raw_data.append(cell.text)    
                    for cell in datacells:
                        raw_odds.append(cell.text)

                # Find all cells in the row

                ML_odds = []
                game_odds = getTodaysGames()
                for game in game_odds:
                    ML_odds.append([game.team1, game.moneyline1])
                    ML_odds.append([game.team2, game.moneyline2])
                

                for team in ML_odds:
                    if(int(team[1]))>0:
                        value = (100/(team[1]+100))*100
                    else:
                        value= ((-1*team[1])/((-1*team[1])+100))*100
                    team.append(value)
                
                n = len(game_odds)
                y = list(self.divide_chunks(raw_odds, 9))

                
            
                for i in range(n*2):
                    for j in range(3):
                        del y[i][0]
                
                #print(y)
                pattern = re.compile(r'([A-Z]{2,3})')
                
            
                # Iterate over the list and extract the matched abbreviation
                abbreviations = [re.search(pattern, item).group(1) for item in raw_data if re.search(pattern, item)]

            # Strings to check for
                strings_to_check = ['EDT', 'PST', 'CDT', 'MDT']

            # Iterate over each string to check
                for string_to_check in strings_to_check:
                
                    if any(string_to_check.lower() in abbreviation.lower() for abbreviation in abbreviations):
                        
                        abbreviations = [abbr for abbr in abbreviations if string_to_check.lower() not in abbr.lower()]

                
                game_splits = []
                for i in range(n):
                    try:
                        # Safely attempt to create GameSplits and add to list if all data is available
                        if len(abbreviations) > 2*i+1 and len(y[i]) >= 6 and len(y[i+1]) >= 6:
                            split = GameSplits(
                                abbreviations[2*i], abbreviations[2*i+1],
                                    y[2*i][0], y[2*i][1], y[2*i][2], y[2*i][3], y[2*i][4], y[2*i][5],
                                    y[2*i+1][0], y[2*i+1][1], y[2*i+1][2], y[2*i+1][3], y[2*i+1][4], y[2*i+1][5]
                            )
                            game_splits.append(split)
                            #print(split)
                    except IndexError as e:
                        print(f"Failed to create GameSplits for team set {i}: {e}")

                
                #print(ML_odds)
                for i in range(len(game_splits)):
                    #        Spread and Over/Under bets
                    #if int(game_splits[i].over_money.strip('%')) >= 90:
                    #    bets.append(Bet(f"{game_splits[i].team1} + {game_splits[i].team2} Under", 1))
                    #elif int(game_splits[i].over_money.strip('%')) <= 10:
                    #    bets.append(Bet(f"{game_splits[i].team1} + {game_splits[i].team2} Over", 1))
                    #if int(game_splits[i].team1_spread_money.strip('%')) <= 30:
                    #    bets.append(Bet(f"{game_splits[i].team1} Spread", 1))
                    #elif int(game_splits[i].team1_spread_money.strip('%')) >= 70:
                    #    bets.append(Bet(f"{game_splits[i].team2} Spread", 1))
                    
                    #       Moneyline bets
                    if (ML_odds[2*i][2] - int(game_splits[i].team1_moneyline_money.strip('%'))) > 10:
                        units = round(1 / (1-abs(ML_odds[2*i][2]/100)) - 1, 1)
                        if(units > 10):
                            units /= 2  
                        bets.append(Bet(f"{ML_odds[2*i][0]}", units))
                    elif(ML_odds[2*i+1][2] - int(game_splits[i].team2_moneyline_money.strip('%'))) > 10:
                        units = round(1 / (1-abs(ML_odds[2*i+1][2]/100)) - 1, 1)
                        if(units > 10):
                            units /= 2  
                        bets.append(Bet(f"{ML_odds[2*i+1][0]}", units))

            else:
                print("No table found on the webpage.")

        else:
            print("Failed to retrieve data. Status code:", response.status_code)

        return bets