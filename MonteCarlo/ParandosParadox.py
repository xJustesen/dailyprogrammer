import random  # for random number generation


class ParandosParadox:
    def __init__(self, epsilon):
        ''' Initalize Parando's paradox. By default the start capital is 100 '''
        self.capital_ = 100
        self.epsilon_ = epsilon
        self.game_won_ = 0
        self.M_ = 3

    def CalculateCapital(self):
        ''' Calculate new capital after game has been played '''
        if self.game_won_:
            self.capital_ = self.capital_ + 1
        else:
            self.capital_ = self.capital_ - 1

    def PlayGameA(self):
        ''' Play game version where win probability is constant '''
        random_uniform_number = random.random()
        win_probability = 0.5 - self.epsilon_
        if random_uniform_number < win_probability:
            self.game_won_ = 1
        else:
            self.game_won_ = 0
        self.CalculateCapital()

    def PlayGameB(self):
        ''' Play game version where win probability depends on capital '''
        random_uniform_number = random.random()
        if (self.capital_ % self.M_ == 0):
            win_probability = 0.1 - self.epsilon_
        else:
            win_probability = 0.75 - self.epsilon_
        if random_uniform_number < win_probability:
            self.game_won_ = 1
        else:
            self.game_won_ = 0
        self.CalculateCapital()

    def GenerateGameOrder(self, number_of_games):
        ''' Generate random order of the two game versions '''
        game_a = [0] * int(number_of_games / 2)
        game_b = [1] * int(number_of_games / 2)
        games = game_a + game_b
        random.shuffle(games)
        return games

    def PlayGame(self, games, number_of_iterations, capital):
        ''' Play Parando's game.
            Input:
                    games                   : Game order (0 : game A, 1 : game B)
                    number_of_iterations    : Number of times the 'games' input is iterated over
                    capital                 : Start capital
        '''
        progress = 0
        average_result = 0
        average_result_game = [0] * (len(games) + 1)
        while progress < number_of_iterations:
            self.capital_ = capital
            for j in range(len(games)):
                if games[j]:
                    self.PlayGameB()
                else:
                    self.PlayGameA()
                average_result_game[j+1] = self.capital_ + \
                    average_result_game[j+1]

            progress += 1
            average_result = average_result + self.capital_

        average_result = average_result / number_of_iterations
        average_result_game[0] = capital * number_of_iterations
        average_result_game = [
            result / number_of_iterations - capital for result in average_result_game]

        return average_result, average_result_game
