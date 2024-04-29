from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


def scrapeNBAOdds():
    export_data = []

    # chrome_options.add_argument("--disable-gpu")
    s = Service("/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(service=s)
    url = "https://sportsbook.draftkings.com/leagues/basketball/nba"
    driver.get(url)

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sportsbook-table"))
    )
    table_body = table.find_element(By.TAG_NAME, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")

    i = 0
    while i < len(rows):
        export_row = []
        row = rows[i]
        team1_name = row.find_element(By.CSS_SELECTOR, "[class*=event-cell__name-text]")
        # print(team1_name.text)
        export_row.append(team1_name.text)
        book_data = row.find_elements(
            By.CSS_SELECTOR, "[class*=sportsbook-outcome-cell__line]"
        )
        for datapoint in book_data:
            export_row.append(datapoint.text)
            # print(datapoint.text)
        i += 1
        row = rows[i]
        team2_name = row.find_element(By.CSS_SELECTOR, "[class*=event-cell__name-text]")
        # print(team2_name.text)
        export_row.insert(1, team2_name.text)
        export_data.append(export_row)
        i += 1

    columns = ["Team 1", "Team 2", "Spread", "Total Points"]
    df = pd.DataFrame(export_data, columns=columns)

    today_date = datetime.today().strftime("%Y-%m-%d")
    file_name = f"../__data__/betting_data_{today_date}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data exported to {file_name}")

    return 1


def getTodaysGames():
    today_date = datetime.today().strftime("%Y-%m-%d")
    file_name = f"../__data__/betting_data_{today_date}.xlsx"

    try:
        # Check if the Excel file exists
        df = pd.read_excel(file_name)
        games = []
        # Iterate through each row in the DataFrame and create a Game object for each row
        for index, row in df.iterrows():
            team1 = row["Team 1"]
            team2 = row["Team 2"]
            ml1 = row["ML1"]
            ml2 = row["ML2"]
            spread = row["Spread"]
            total_points = row["Total Points"]
            games.append(Game(team1, team2, ml1, ml2, spread, total_points))
        return games

    except FileNotFoundError:
        # If the file does not exist, call scrapeNBAOdds()
        print(f"Excel file {file_name} not found. Need to scrape NBA odds")

def getYesterdayResults():     
    export_data = []

    # chrome_options = Options()
    # chrome_options.add_argument("--disable-gpu")
    s = Service('/usr/local/bin/chromedriver') 

    driver = webdriver.Chrome(service=s)
    url = 'https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange=2014-02-10'
    driver.get(url)

    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id*=scoreboard-group-2]")))
    all_lists = table.find_elements(By.TAG_NAME, "ul")

    if(len(all_lists) == 0):
        print("No games found on this date")
        return pd.DataFrame()
    
    list = all_lists[0]
    games = list.find_elements(By.TAG_NAME, "li")
    for game in games:
        data = game.find_elements(By.TAG_NAME, "li")

        for i in range(0, len(data), 2):
            # print(data[i].text)
            team1_first = data[i].find_element(By.CSS_SELECTOR, 'span[data-tst="first-name"]').text
            team1_last = data[i].find_element(By.CSS_SELECTOR, 'span[data-tst="last-name"]').text
            team1_score = data[i].find_element(By.CSS_SELECTOR, 'div[class*="Whs(nw)"]').text

            team2_first = data[i+1].find_element(By.CSS_SELECTOR, 'span[data-tst="first-name"]').text
            team2_last = data[i+1].find_element(By.CSS_SELECTOR, 'span[data-tst="last-name"]').text
            team2_score = data[i+1].find_element(By.CSS_SELECTOR, 'div[class*="Whs(nw)"]').text

            export_data.append([team1_first, team1_last, team1_score, team2_first, team2_last, team2_score])

            # print (team1_first)
            # print (team1_last)
            # print(team1_score)



    columns = ["Team 1 First", "Team 1 Last", "Team 1 Score", "Team 2 First", "Team 2 Last", "Team 2 Score"]
    df = pd.DataFrame(export_data, columns=columns)

    return df
        