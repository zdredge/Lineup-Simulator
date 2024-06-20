import itertools
from typing import List

from Player import Player

outfield = []
first_base = []
second_base = []
third_base = []
shortstop = []
catcher = []
designated_hitter = []


def create_lineup(player_lst):
    sort_positionally(player_lst)
    subsets = generate_subsets()
    lineups = cartesian_product(subsets)
    lineups = remove_invalid_lineups(lineups)

    print("# valid lineups: ", len(lineups))
    return 0


def sort_positionally(player_lst):
    for player in player_lst:
        for position in player.positions:
            if position == "OF":
                outfield.append(player)
            elif position == "1B":
                first_base.append(player)
            elif position == "2B":
                second_base.append(player)
            elif position == "3B":
                third_base.append(player)
            elif position == "SS":
                shortstop.append(player)
            elif position == "C":
                catcher.append(player)
            elif position == "DH":
                designated_hitter.append(player)

    # print("Outfielders: ")
    # for player in outfield:
    #     print(str(player))
    #
    # print("First basemen: ")
    # for player in first_base:
    #     print(str(player))
    #
    # print("Second basemen: ")
    # for player in second_base:
    #     print(str(player))
    #
    # print("Third basemen: ")
    # for player in third_base:
    #     print(str(player))
    #
    # print("Shortstops: ")
    # for player in shortstop:
    #     print(str(player))
    #
    # print("Catchers: ")
    # for player in catcher:
    #     print(str(player))


def generate_subsets():
    player_pool = list()
    # choose OF
    player_pool.append(subsets_of_size(outfield, 3))
    # choose 1B
    player_pool.append(subsets_of_size(first_base, 1))

    # choose 2B
    player_pool.append(subsets_of_size(second_base, 1))

    # choose 3B
    player_pool.append(subsets_of_size(third_base, 1))

    # choose SS
    player_pool.append(subsets_of_size(shortstop, 1))

    # choose C
    player_pool.append(subsets_of_size(catcher, 1))

    player_pool.append(subsets_of_size(designated_hitter, 1))

    return player_pool


def subsets_of_size(given_set, subset_size):
    # Generate all subsets of the specified size
    subsets = list(itertools.combinations(given_set, subset_size))

    return subsets


def cartesian_product(position_subsets):
    lineups = list(itertools.product(position_subsets[0], position_subsets[1], position_subsets[2], position_subsets[3],
                                     position_subsets[4], position_subsets[5], position_subsets[6]))
    return lineups


def remove_invalid_lineups(lineups: List[Player]):
    invalid_lineups = list()
    for lineup in lineups:
        names = list()
        for players in lineup:
            for player in players:
                if player.name in names:
                    invalid_lineups.append(lineup)
                else:
                    names.append(player.name)

    invalid_lineups = list(set(invalid_lineups))
    print("# invalid lineups: ", len(invalid_lineups))

    for lineup in invalid_lineups:
        lineups.remove(lineup)

    return lineups

