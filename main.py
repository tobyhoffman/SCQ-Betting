
import pandas as pd

masterUrl = "https://stathead.com/tiny/ELmeC"

# store team stats as strings

mastertable = pd.read_html(masterUrl)[0]

#parse tables from html - stored as var

mastertable.to_excel("MasterStats.xlsx")
mastertable = pd.read_excel("MasterStats.xlsx", header=1)
mastertable.to_excel("MasterStats.xlsx")

# Store the teams stats in Excel file

def offensiveRating(team):
    oetable = pd.read_excel('MasterStats.xlsx')
    row_index = oetable.index[oetable['Team'] == team].tolist()

    return (oetable['ORtg'].iloc[row_index[0]])


def defensiveRating(team):
    detable = pd.read_excel('MasterStats.xlsx')
    row_index = detable.index[detable['Team'] == team].tolist()

    return (detable['DRtg'].iloc[row_index[0]])

def pointsPerGame(team):
    ppgtable = pd.read_excel('MasterStats.xlsx')
    row_index = ppgtable.index[ppgtable['Team'] == team].tolist()

    return ((ppgtable['ORtg'].iloc[row_index[0]]) / 100 * (ppgtable['Pace'].iloc[row_index[0]]))

def trueShootingPercentage(team):
    tsptable = pd.read_excel('MasterStats.xlsx')
    row_index = tsptable.index[tsptable['Team'] == team].tolist()

    return (tsptable['TS%'].iloc[row_index[0]])

def turnoverPercentage(team):
    totable = pd.read_excel('MasterStats.xlsx')
    row_index = totable.index[totable['Team'] == team].tolist()

    return (totable['TOV%'].iloc[row_index[0]])

def marginOfVictory(team):
    asmtable = pd.read_excel('MasterStats.xlsx')
    row_index = asmtable.index[asmtable['Team'] == team].tolist()

    return (asmtable['MOV'].iloc[row_index[0]])


def project(team1, team2):

    if (defensiveRating(team1) + offensiveRating(team1)) > ((defensiveRating(team2) + offensiveRating(team2))):
        return team1
    else:
        return team2


if __name__ == '__main__':

    print(project('DAL','IND'))
