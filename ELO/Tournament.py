from EloRating import EloRating


class Tournament:
    def __init__(self, ratings, results):
        self.player_ratings = ratings
        self.results = results
        self.number_of_players = len(ratings)

    def UpdateEloScores(self):
        # Iterate over all players in the tournament
        for i in range(self.number_of_players):
            # Retrieve rating and actual score of player
            rating_a = self.player_ratings[i]
            expected_score = 0.0
            actual_score = sum(self.results[i])
            # Calculate expected score from player
            for j in range(self.number_of_players):
                rating_b = self.player_ratings[j]
                if (i != j):
                    elo = EloRating(rating_a, rating_b)
                    expected_score += elo.CalculateExpectedScore()
            # Adjust players ELO rating
            self.player_ratings[i] = elo.AdjustEloRating(
                rating_a, actual_score, expected_score)

    def CalculatePerformanceRating(self, games_played, total_opponent_rating, wins, losses):
        ''' Calculate the FIDE performance rating of a player '''
        return (total_opponent_rating + 400.0 * (wins - losses)) / games_played

    def GetPerformanceRating(self, player_id):
        # Iterate over all players in the tournament
        total_opponent_rating = 0
        for i in range(self.number_of_players):
            if (i == player_id):
                for j in range(self.number_of_players):
                    if (i != j):
                        total_opponent_rating += self.player_ratings[j]
                games_played = len(self.results[i])
                wins = sum(self.results[i])
                losses = games_played - wins
                return self.CalculatePerformanceRating(games_played, total_opponent_rating, wins, losses)

    def GetPerformanceRatings(self):
        performance_ratings = [0] * self.number_of_players
        for i in range(self.number_of_players):
            performance_ratings[i] = self.GetPerformanceRating(i)
        return performance_ratings

    def EstimateUSCFKfactor(self, effective_games_played, tournament_games_played):
        ''' Use the USCF method to estimate the K factor '''
        return 800.0 / (effective_games_played + tournament_games_played)
