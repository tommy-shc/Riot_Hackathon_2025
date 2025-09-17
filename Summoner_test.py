import requests
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY  = os.getenv("APIKEY")

class Summoner:
    def __init__(self, gameName, tagLine="NA1"):
        self.gameName = gameName
        self.tagLine = tagLine
        self.account = self.get_summoner_by_name()
        self.puuid = self.account['puuid']

    def get_summoner_by_name(self):
        url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{self.gameName}/{self.tagLine}?api_key=" + APIKEY

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

summoner = Summoner("dump1ng0d", "lol")


print(f"Summoner IGN: {summoner.gameName} summoner puuid: {summoner.puuid}")