from Player import Player


class Team:
    def __init__(self, points=500, form=0.5, team_id=9999, name="N/A"):
        self.form = form
        self.id = team_id
        self.points = points
        self.name = name
        self.player_list = []

    def AddPlayer(self, player_name, stats, player_id):
        player_obj = Player(player_name, stats, player_id)
        self.player_list.append(player_obj)

    def CalculateTeamRating(self):
        rating = 0.0
        for player in self.player_list:
            rating += player.stats['Rating 2.0']
        return rating/len(self.player_list)
