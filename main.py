# This is a sample Python script.
import CreateLineup
from Player import Player


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    offensive_stats = {
        "AVG": 350,
        "OBP": 500,
        "OPS": 1.200
    }
    defensive_stats = {
        "E": 22,
        "A": 120,
    }
    deacon = Player("Deacon", ["C", "3B", "1B", "DH"], {"AVG": 421, "OBP": 528, "OPS": 1072}, {"E": 6, "A": 9})
    pierce = Player("Pierce", ["2B", "DH"], {"AVG": 327, "OBP": 435, "OPS": 782}, {"E": 6, "A": 9})
    brock = Player("Brock", ["OF", "DH"], {"AVG": 324, "OBP": 489, "OPS": 901}, {"E": 6, "A": 9})
    parker = Player("Parker", ["1B", "DH"], {"AVG": 308, "OBP": 451, "OPS": 810}, {"E": 6, "A": 9})
    kelstin = Player("Kelstin", ["OF", "DH"], {"AVG": 305, "OBP": 423, "OPS": 812}, {"E": 6, "A": 9})
    jason = Player("Jason", ["3B", "SS", "2B", "1B", "DH"], {"AVG": 300, "OBP": 417, "OPS": 767}, {"E": 6, "A": 9})
    ezra = Player("Ezra", ["OF", "DH"], {"AVG": 293, "OBP": 382, "OPS": 831}, {"E": 6, "A": 9})
    tim = Player("Tim", ["OF", "SS", "2B", "DH"], {"AVG": 267, "OBP": 389, "OPS": 722}, {"E": 6, "A": 9})
    jayse = Player("Jayse", ["SS", "DH"], {"AVG": 227, "OBP": 424, "OPS": 719}, {"E": 6, "A": 9})
    rohan = Player("Rohan", ["OF", "DH"], {"AVG": 225, "OBP": 385, "OPS": 635}, {"E": 6, "A": 9})
    ryan = Player("Ryan", ["C", "DH"], {"AVG": 136, "OBP": 269, "OPS": 406}, {"E": 6, "A": 9})
    zammit = Player("Zammit", ["1B", "DH"], {"AVG": 105, "OBP": 320, "OPS": 425}, {"E": 6, "A": 9})
    jackson = Player("Jackson", ["2B", "DH"], {"AVG": 000, "OBP": 000, "OPS": 000}, {"E": 6, "A": 9})

    players = list({deacon, pierce, brock, parker, kelstin, jason, ezra, tim, jayse, rohan, ryan, zammit, jackson})

    #print(players)

    l1 = CreateLineup.create_lineup(players)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
