import requests

standings_url = "https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"

data = requests.get(standings_url) ## getting html of website

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text) ##parsing html into beautiful soup

##css selector
standings_table = soup.select("table.stats_table")[0]

links = standings_table.find_all('a')

links = [l.get('href') for l in links]

links = [l for l in links if '/squads' in l]

team_urls = [f"https://fbref.com{l}" for l in links]

import pandas as pd
team_url = team_urls[0]
data = requests.get(team_url)
matches = pd.read_html(data.text, match="Standard Stats ")
matches[0].columns = matches[0].columns.droplevel()
print(matches[0].head()) 