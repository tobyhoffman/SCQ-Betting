class Game:
    def __init__(self, team1, team2, team1_odds, team2_odds, spread, total):
        self.team1 = team1
        self.team2 = team2
        self.moneyline1 = team1_odds
        self.moneyline2 = team2_odds
        self.spread = spread
        self.total = total

    def __str__(self):
        return f"Team 1: {self.team1}, Team 2: {self.team2}, Moneyline 1: {self.moneyline1}, Moneyline 2: {self.moneyline2}, Spread: {self.spread}, Total Points: {self.total}"