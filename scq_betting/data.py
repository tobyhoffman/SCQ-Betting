from datetime import datetime

import pandas as pd

from game import Game

masterUrl = "https://stathead.com/tiny/i2XKf"

# store team stats as strings

mastertable = pd.read_html(masterUrl)[0]

# parse tables from html - stored as var

mastertable.to_excel("../__data__/MasterStats.xlsx")
mastertable = pd.read_excel("../__data__/MasterStats.xlsx", header=1)
mastertable.to_excel("../__data__/MasterStats.xlsx")

# Store the teams stats in Excel file


def offensiveRating(team):
    oetable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = oetable.index[oetable["Team"] == team].tolist()

    return oetable["ORtg"].iloc[row_index[0]]


def defensiveRating(team):
    detable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = detable.index[detable["Team"] == team].tolist()

    return detable["DRtg"].iloc[row_index[0]]


def pointsPerGame(team):
    ppgtable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = ppgtable.index[ppgtable["Team"] == team].tolist()

    return (
        (ppgtable["ORtg"].iloc[row_index[0]])
        / 100
        * (ppgtable["Pace"].iloc[row_index[0]])
    )


def trueShootingPercentage(team):
    tsptable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = tsptable.index[tsptable["Team"] == team].tolist()

    return tsptable["TS%"].iloc[row_index[0]]


def turnoverPercentage(team):
    totable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = totable.index[totable["Team"] == team].tolist()

    return totable["TOV%"].iloc[row_index[0]]


def marginOfVictory(team):
    asmtable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = asmtable.index[asmtable["Team"] == team].tolist()

    return asmtable["MOV"].iloc[row_index[0]]


def winPercentage(team):
    wpmtable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = wpmtable.index[wpmtable["Team"] == team].tolist()

    return wpmtable["W/L%"].iloc[row_index[0]]


def strengthOfSchedule(team):
    stptable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = stptable.index[stptable["Team"] == team].tolist()

    return (stptable["SOS"]).iloc[row_index[0]]


def simpleRating(team):
    rattable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = rattable.index[rattable["Team"] == team].tolist()

    return (rattable["SRS"]).iloc[row_index[0]]


def freeThrowAttemptRate(team):
    ftrttable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = ftrttable.index[ftrttable["Team"] == team].tolist()

    return (ftrttable["FTr"]).iloc[row_index[0]]


def freeThrowPercentage(team):
    ftptable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = ftptable.index[ftptable["Team"] == team].tolist()

    return (ftptable["FT%"]).iloc[row_index[0]]


def offensiveReboundPercentage(team):
    orptable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = orptable.index[orptable["Team"] == team].tolist()

    return (orptable["ORB%"]).iloc[row_index[0]]


def defensiveReboundPercentage(team):
    drptable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = drptable.index[drptable["Team"] == team].tolist()

    return (drptable["DRB%"]).iloc[row_index[0]]

def pace(team):
    pacetable = pd.read_excel("../__data__/MasterStats.xlsx")
    row_index = pacetable.index[pacetable["Team"] == team].tolist()

    return (pacetable["Pace"]).iloc[row_index[0]]
def getTodaysGames():

    file_name = f"../__data__/betting_data.xlsx"

    try:
        # Check if the Excel file exists
        df = pd.read_excel(file_name)
        games = []
        # Iterate through each row in the DataFrame and create a Game object for each row
        for index, row in df.iterrows():
            team1 = row['Team 1']
            team2 = row['Team 2']
            ml1 = row['ML1']
            ml2 = row['ML2']
            spread = row['Spread']
            total_points = row['Total Points']
            games.append(Game(team1, team2, ml1, ml2, spread, total_points))
        return games

    except FileNotFoundError:
        # If the file does not exist, call scrapeNBAOdds()
        print(f"Excel file {file_name} not found. Need to scrape NBA odds")
