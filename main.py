import pandas as pd

url = "https://www.teamrankings.com/nba/stat/offensive-efficiency"
url2 = "https://www.teamrankings.com/nba/stat/true-shooting-percentage"
url3 = "https://www.teamrankings.com/nba/stat/turnover-pct"
url4 = "https://www.teamrankings.com/nba/stat/points-per-game"
url5 = "https://www.teamrankings.com/nba/stat/defensive-efficiency"
url6 = "https://www.teamrankings.com/nba/stat/average-scoring-margin"

# store team stats as strings

table = pd.read_html(url)[0]
table2 = pd.read_html(url2)[0]
table3 = pd.read_html(url3)[0]
table4 = pd.read_html(url4)[0]
table5 = pd.read_html(url5)[0]
table6 = pd.read_html(url6)[0]

#parse tables from html - stored as var


table[['Team', '2023']].to_excel("oe.xlsx")
table2[['Team', '2023']].to_excel("ts.xlsx")
table3[['Team', '2023']].to_excel("to.xlsx")
table4[['Team', '2023']].to_excel("ppg.xlsx")
table5[['Team', '2023']].to_excel("de.xlsx")
table6[['Team', '2023']].to_excel("asm.xlsx")

# Store the teams stats in Excel files

def offensiveEfficiency(team):
    oetable = pd.read_excel('oe.xlsx')
    row_index = oetable.index[oetable['Team'] == team].tolist()

    return (oetable['2023'].iloc[row_index[0]])


def defensiveEfficiency(team):
    detable = pd.read_excel('de.xlsx')
    row_index = detable.index[detable['Team'] == team].tolist()

    return (detable['2023'].iloc[row_index[0]])

def project(team1, team2):

    if (defensiveEfficiency(team1) + offensiveEfficiency(team1)) > ((defensiveEfficiency(team2) + offensiveEfficiency(team2))):
        return team1
    else:
        return team2


print(project('Denver','Indiana'))




