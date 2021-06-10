
from requests.models import Response
import seaborn as sns
import pandas as  pd
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import os
from dotenv import load_dotenv

# Environment variables 
load_dotenv()
MY_API_KEY = os.getenv("MY_API_KEY")
MY_API_HOST = os.getenv("MY_API_HOST")

season = ""
RAPIDAPI_KEY = MY_API_KEY
RAPIDAPI_HOST = MY_API_HOST

url = "https://api-nba-v1.p.rapidapi.com"
headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,
    'x-rapidapi-host': RAPIDAPI_HOST
}

inputdata = {}
inputdata["teams"] = []
inputdata["result"] = []
inputdata["win-loss"] = []


def fetchStandingsData(year):
    response = requests.request("GET", url + "/standings/standard" + year, headers=headers)
    
    if response.code == 200:
        return response.body
    else:
        return None

def fetchTeamNames(teamId):
    response = requests.request("GET", url+"/teams/teamId"+teamId, headers)
    if response.code == 200:
        return response.body["api"]["teams"][0]["fullName"]
    else:
        return None

if __name__ == "__main__":
    try:
        while len(season) <= 2:
            season = input("Enter the NBA Season (Year) you want to view the stats for: ")
        response = fetchStandingsData(season)
        print('response:', response)

        if None != response:
            standings_data = response['api']['standings']
            print(standings_data)
            for team_data in standings_data:
                print('team:', team_data)
                team_name = fetchTeamNames(team_data["teamId"])
    finally:
        print('done')

