# This is a sample Python script.
import CreateLineup
import GameSim
import SummaryStatistics
from Player import Player
from readCSV import read_csv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def strip_tuple(lineup: tuple):
    master_lineup = []
    for i in range(7):
        if i == 0:
            for j in range(3):
                master_lineup.append(lineup[i][j])
        else:
            master_lineup.append(lineup[i][0])


    return master_lineup



if __name__ == '__main__':

    hard_coded_positions = [["OF", "DH"], ["OF", "DH"], ["OF", "DH"], ["P", "2B", "DH"], ["P", "1B", "DH"], ["P"], ["P"], ["P"],
                            ["3B", "SS", "2B", "1B", "DH"], ["3B", "1B", "C", "DH"], ["P"], ["OF", "P", "DH"], ["2B", "DH"], ["SS", "DH"],
                            ["C", "DH"], ["1B", "DH"], ["OF", "DH"]]

    players = read_csv('16u 2024 Midwestern Ontario Bearcats Summer 2024 Stats (1).csv')

    # for player in players:
    #     positions = input("For " + player.name + ", please enter their positions seperated by a comma (E.g. C, 1B, 3B): ")
    #
    #     positions_lst = list(positions.split(","))
    #     print(positions)
    #     player.positions = positions

    for i in range(len(players)):
        players[i].positions = hard_coded_positions[i]

    # for player in players:
    #     print(player)

    l1 = CreateLineup.create_lineup(list(players)) # in the form ((OF), (1B), (2B), (3B), (SS), (C), (DH))

    for i in range(len(l1)):
        for j in range(44):
            lineup = strip_tuple(l1[i])
            SummaryStatistics.update_current_run(GameSim.run_sim(lineup), lineup)
        SummaryStatistics.update_rankings()

    print("TOP LINEUP: ")

    for i in range(9):
        print("LINEUP #", i)
        for j in range(9):

            print(SummaryStatistics.TOP_LINEUPS[i][j].__str__())
        print("RUNS SCORED: ", SummaryStatistics.TOP_RUNS_PER_GAME[i])
    # lineup = strip_tuple(l1[i])
    # GameSim.run_sim(lineup)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
