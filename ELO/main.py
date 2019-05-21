from Tournament import Tournament
from EloRating import EloRating
import math

# Define ratings for tournament players
Player0 = 1613.0
Player1 = 1609.0
Player2 = 1477.0
Player3 = 1388.0
Player4 = 1586.0
Player5 = 1720.0

players = ["Player0", "Player1", "Player2", "Player3", "Player4", "Player5"]
ratings = [Player0, Player1, Player2, Player3, Player4, Player5]
results = [[0, 0.5, 1, 1, 0], [1, 1, 1, 1, 0], [0.5, 0, 1, 1, 0],
           [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 1]]
record = ["X L D W W L", "W X W W W L", "D L X W W L",
          "L L L X L L", "L L L W X L", "W W W W W X"]

# Initialise Swiss Tournament
tournament = Tournament(ratings, results)
performance_ratings = tournament.GetPerformanceRatings()
old_ratings = ratings.copy()
tournament.UpdateEloScores()

# Print results
print("Rating:\tprev\tnew\tperformance\trecord")
for i in range(len(players)):
    print(players[i] + "\t{}\t{}\t{}".format(math.floor(old_ratings[i]),
                                             math.floor(ratings[i]),
                                             math.floor(performance_ratings[i])) + "\t\t" + record[i])
