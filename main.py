
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

url = "https://free-nba.p.rapidapi.com/teams"
headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,
    'x-rapidapi-host': RAPIDAPI_HOST
}
querystring = {"page":"0"}

inputdata = {}
inputdata["teams"] = []
inputdata["result"] = []
inputdata["win-loss"] = []


def fetchStandingsData(year):
    response = requests.request("GET", url + "/standings/standard" + year, headers=headers, params=querystring)
    print('response text:', response.text)

def fetchTeamNames(teamId):
    response = requests.request("GET", url+"/teams/teamId"+teamId, headers=headers, params=querystring)
    print(response.text)

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

                inputdata["teams"].append(team_name)
                inputdata["result"].append("win")
                inputdata["win-loss"].append(int(team_data["win"]))

                inputdata['teams'].append(team_name)
                inputdata['result'].append('loss')
                inputdata['win-loss'].append(int(team_data['loss']))

                print("Team:", team_name)
                print("W-L: " + team_data['win'] + " - " + team_data['loss'])
                print("\n")
            
            df = pd.DataFrame(inputdata)
            print(df)
    
    except Exception as e:
        print("Errorhere")  
        print(e)

