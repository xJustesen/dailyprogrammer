#!/bin/python3

import ParandosParadox as pp
import matplotlib.pyplot as plt  # for plotting


def LinSpace(start, end, steps):
    '''
    Linearly spaced list of numbers
    Input:
            start   : first number in list
            end     : last number in list
            steps   : number of numbers in list
    '''
    step_size = (end - start) / steps
    linspace = [0] * steps
    for step in range(steps - 1):
        linspace[step] = start + step * step_size
    linspace[-1] = end
    return linspace


# Initialize ParandosParadox class
print("Preparing experiment")
number_of_iterations = 50000
number_of_games = 2 * 100
start_capital = 100.0
game = pp.ParandosParadox(0.005)
game_order_mixed = game.GenerateGameOrder(number_of_games)
game_order_A = [0] * number_of_games
game_order_B = [1] * number_of_games
number_of_games_array = LinSpace(
    0, number_of_games + 1, number_of_games + 1)

# Run experiment with three different game orders
print("Running experiment")
end_capital_mixed, average_capital_mixed = game.PlayGame(
    game_order_mixed, number_of_iterations, start_capital)
end_capital_A, average_capital_A = game.PlayGame(
    game_order_A, number_of_iterations, start_capital)
end_capital_B, average_capital_B = game.PlayGame(
    game_order_B, number_of_iterations, start_capital)

# Plot average capital won as function of number of games played
print("Plotting results")
plt.figure()
plt.plot(number_of_games_array, average_capital_mixed, 'g-', label='Mixed')
plt.plot(number_of_games_array, average_capital_A, 'b-', label='Game A')
plt.plot(number_of_games_array, average_capital_B, 'r-', label='Game B')
plt.legend()
plt.xlabel("Number of games")
plt.ylabel("Average winnings")
plt.title("Start captial = {:3.1f} ; Epsilon = {:1.3f} ; M = {:d} ; Iterations = {:d}".format(start_capital,
                                                                                              0.005, 3, number_of_iterations))
plt.show()

print("Finished.")
