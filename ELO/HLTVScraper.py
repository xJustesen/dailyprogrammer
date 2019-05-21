#!bin/sh/python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from Team import Team as Team_
from NumbersToMonth import NumbersToMonth


class HLTVScraper:

    def __init__(self, y, m, d):
        '''
        Class constructor for HLTV scraper.
        Input:
            y : year, fx. 2019
            m : month, fx. 04
            d : day, fx. 26
        '''
        month_int = int(m)
        converter = NumbersToMonth()
        month_name = converter.numbers_to_months(month_int)
        self.startDate = y + '-' + str(month_int - 3) + '-' + d
        self.endDate = y + '-' + m + '-' + d
        # URL for top twenty rankings
        self.top_twenty_page = 'https://www.hltv.org/ranking/teams/' + y + '/' + month_name + '/' + d
        # pretend to be a chrome 47 browser on a windows 10 machine (circumvents HTTP 403 forbidden response)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

    def SetStartDate(self, start_date):
        self.startDate = start_date

    def SetEndDate(self, end_date):
        self.endDate = end_date

    def GetHLTVTopTwenty(self):
        # Query website and export HTML page
        req = Request(self.top_twenty_page, headers=self.headers)
        page = urlopen(req)
        # Parse HTML page using beautiful soup
        soup = BeautifulSoup(page, 'html.parser')
        # Get team names, id and points
        team_points = self.GetTeamPoints(soup)
        team_names = self.GetTeamNames(soup)
        team_id = self.GetTeamId(soup)
        teams = [team_names, team_id, team_points]
        return teams

    def GetTeamNames(self, soup):
        teams = soup.find_all("span", class_="name")
        team_names = []
        for team in teams:
            team_names.append(team.string)
        return team_names

    def GetTeamPoints(self, soup):
        # Take out <span> 'points' and get their value
        team_points = soup.find_all("span", class_="points")
        # Clean points string
        team_points_formatted = []
        for points in team_points:
            points.string = points.string[(points.string.find("(") + 1): points.string.rfind(" ")]
            team_points_formatted.append(points.string)
        return team_points_formatted

    def GetTeamId(self, soup):
        team_logo = soup.find_all("span", class_="team-logo")
        # Extract team-id from team_logo
        team_id = []
        for team in team_logo:
            id_as_string = str(team.contents)
            team_id.append(id_as_string[id_as_string.find("logo/") + len("logo/"): id_as_string.rfind('" title="')])
        return team_id

    def GetTeamPlayers(self, team_name, team_id):
        team_url = "https://www.hltv.org/team/" + team_id + "/" + team_name
        # Query website and export HTML page
        req = Request(team_url, headers=self.headers)
        page = urlopen(req)
        # Parse HTML page using beautiful soup
        soup = BeautifulSoup(page, 'html.parser')
        team_players = soup.find_all(href=re.compile("/player/"))
        players = []
        for player in team_players:
            # Retriever player name and replace spaces by '%20'
            player_name = player.get('title')
            player_name = player_name.replace(" ", "%20")
            # player_id = player.get('href')[8:player.get('href').rfind("/" + player.get('title'))]
            player_id = player.get('href')[8:(len(player.get('href')) - len(player_name) - 1)]
            # Retriever player stats
            player_stats_url = "https://www.hltv.org/stats/players/" + player_id + "/" + player_name + "?startDate=" + \
                self.startDate + "&endDate=" + self.endDate + "&matchType=BigEvents&rankingFilter=Top20"
            req = Request(player_stats_url, headers=self.headers)
            player_stats_page = urlopen(req)
            player_soup = BeautifulSoup(player_stats_page, 'html.parser')
            statistics = player_soup.find_all("div", class_="stats-row")
            player_stats = {}
            for stat in statistics:
                player_stats[stat.contents[0].string] = stat.contents[1].string
            players.append([player_name, player_id, player_stats])
        return players


# Scrape data for top 20 CSGO teams according to HLTV.org
data = HLTVScraper('2019', '04', '15')
teams = data.GetHLTVTopTwenty()

# Define generators to retrieve team players
player_gen = (data.GetTeamPlayers(teams[0][i], teams[1][i]) for i in range(20))
# Make Team class instance for each team
Team = {teams[0][i]: Team_(teams[2][i], 0.5, teams[1][i], teams[0][i]) for i in range(20)}

# Add players to each team
for key, value in Team.items():
    players = next(player_gen)
    for player in players:
        Team[key].AddPlayer(player[0], player[2], player[1])
    print("Added players to " + Team[key].name)
