from scq_betting.bet import Bet
from scq_betting.data import *
from scq_betting.game import Game


class Algorithm:
    def __init__(self):
        # Initialize any parameters or variables needed for your betting strategy
        pass

    def run(self):
        # Implement your betting strategy here
        bets = []

        todays_games = (
            getTodaysGames()
        )  # getTodaysGames() returns a list of Game objects

        for game in todays_games:
            team1 = game.team1
            team2 = game.team2

            if (offensiveRating(team1) > offensiveRating(team2) 
                and defensiveRating(team1) > defensiveRating(team2)):
                bets.append(Bet(team1, 2))  # bet a fixed wager of 2 units on team1
            
            elif (offensiveRating(team2) > offensiveRating(team1) 
                  and defensiveRating(team2) > defensiveRating(team1)):
                bets.append(Bet(team2, 2)) #bet a fixed wager of 2 units on team2

        return bets  # return the bets that your strategy determines
