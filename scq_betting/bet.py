# bet.py


class Bet:
    def __init__(self, team, wager):
        self.team = team
        self.wager = wager

    def __str__(self):
        return f"Betting on {self.team} with a wager of {self.wager}"


"""
Team Names must be of the format:
BOS
OKC
LAL
NYK
ORL
PHI
...

"""
