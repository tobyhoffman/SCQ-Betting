from bet import Bet
from game import Game
from data import *


class Algorithm:
    def __init__(self):
        # Initialize any parameters or variables needed for your betting strategy
        pass

    def run(self):

        # Implement your betting strategy here
        bets = []

        todays_games = getTodaysGames()  # getTodaysGames() returns a list of Game objects

        for game in todays_games:
            team1 = game.team1
            team2 = game.team2
            
            if (offensiveEfficiency(team1) > offensiveEfficiency(team2) and defensiveEfficiency(team1) > defensiveEfficiency(team2)):
                bets.append(Bet(team1, 2))  # bet a fixed wager of 2 units on team1
            
            elif (offensiveEfficiency(team2) > offensiveEfficiency(team1) and defensiveEfficiency(team2) > defensiveEfficiency(team1)):
                bets.append(Bet(team2, 2)) #bet a fixed wager of 2 units on team2

        
        return bets # return the bets that your strategy determines
