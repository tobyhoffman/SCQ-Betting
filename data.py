import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from game import Game


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


def scrapeNBAOdds():     
    export_data = []
    
    # chrome_options.add_argument("--disable-gpu")
    s = Service('/usr/local/bin/chromedriver') 

    driver = webdriver.Chrome(service=s)
    url = 'https://sportsbook.draftkings.com/leagues/basketball/nba'
    driver.get(url)

    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sportsbook-table")))
    table_body = table.find_element(By.TAG_NAME, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")

    i = 0
    while i < len(rows):
        export_row = []
        row = rows[i]
        team1_name = row.find_element(By.CSS_SELECTOR, "[class*=event-cell__name-text]")
        # print(team1_name.text)
        export_row.append(team1_name.text)
        book_data = row.find_elements(By.CSS_SELECTOR, "[class*=sportsbook-outcome-cell__line]")
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

    today_date = datetime.today().strftime('%Y-%m-%d')
    file_name = f"betting_data_{today_date}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data exported to {file_name}")
    
    return 1

def getTodaysGames():
    today_date = datetime.today().strftime('%Y-%m-%d')
    file_name = f"betting_data_{today_date}.xlsx"

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
        
    
