from scq_betting.data import getTodaysGames

games = getTodaysGames()

for game in games:
    print(game)
