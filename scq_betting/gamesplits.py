class GameSplits:
    def __init__(self, team1, team2, team1_spread_money, team1_spread_bet, 
           team1_moneyline_money, team1_moneyline_bet, over_money, over_bet, 
           team2_spread_money, team2_spread_bet, team2_moneyline_money, 
           team2_moneyline_bet, under_money, under_bet):
      self.team1 = team1
      self.team2 = team2
      self.team1_spread_money = team1_spread_money
      self.team1_spread_bet = team1_spread_bet
      self.team1_moneyline_money = team1_moneyline_money
      self.team1_moneyline_bet = team1_moneyline_bet
      self.over_money = over_money
      self.over_bet = over_bet
      self.team2_spread_money = team2_spread_money
      self.team2_spread_bet = team2_spread_bet
      self.team2_moneyline_money = team2_moneyline_money
      self.team2_moneyline_bet = team2_moneyline_bet
      self.under_money = under_money
      self.under_bet = under_bet

    def __str__(self):
        return f"Team 1: {self.team1}, Team 2: {self.team2}, Team 1 Spread Money % 1: {self.team1_spread_money}, " \
           f"Team 1 Spread Bet %: {self.team1_spread_bet}, Team 1 Moneyline Money %: {self.team1_moneyline_money}, " \
           f"Team 1 Moneyline Bet %: {self.team1_moneyline_bet}, Over Money %: {self.over_money}, " \
           f"Over Bet %: {self.over_bet}, Team 2 Spread Money %: {self.team2_spread_money}, " \
           f"Team 2 Spread Bet %: {self.team2_spread_bet}, Team 2 Moneyline Money %: {self.team2_moneyline_money}, " \
           f"Team 2 Moneyline Bet %: {self.team2_moneyline_bet}, Under Money %: {self.under_money}, " \
           f"Under Bet %: {self.under_bet}"