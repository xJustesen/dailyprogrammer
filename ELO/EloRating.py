class EloRating:
    def __init__(self, Ra=1000, Rb=1000, K=32):
        self.rating_player_a = Ra
        self.rating_player_b = Rb
        self.K = K
        self.win_probability_a = self.CalculateExpectedScore()
        self.win_probability_b = 1.0 - self.win_probability_a

    def SetEloScores(self, Ra, Rb):
        self.rating_player_a = Ra
        self.rating_player_b = Rb

    def CalculateExpectedScore(self):
        ''' Calcuate the expected score (ie. win probability) for player A '''
        return 1.0/(1.0+pow(10, (self.rating_player_b-self.rating_player_a)/400.0))

    def AdjustEloRating(self, rating, actual_score, expected_score):
        ''' Calculate the adjusted score for a player '''
        return rating+self.K * (actual_score-expected_score)

    def PrintWinProbability(self):
        print("Probability that team A wins: {}\nProbability that team B wins: {}".format(
            self.win_probability_a, self.win_probability_b))
