class Player:
    def __init__(self, player_name=None, stats={"stats": None}, player_id=None):
        self.id = player_id
        self.name = player_name
        self.stats = stats
