import csv

from Player import Player

offensive_stat_ids = []
defensive_stat_ids = []
pitching_stat_ids = []

players = []
def read_csv(file_path: str) -> None:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if "Number" in row:
                for i in range(3, 54, 1):
                    offensive_stat_ids.append(row[i])
                #print(offensive_stat_ids)

                for j in range(55, 142, 1):
                    pitching_stat_ids.append(row[j])
                #print(pitching_stat_ids)

                for z in range(143, 157, 1):
                    defensive_stat_ids.append(row[z])
                #print(defensive_stat_ids)

            if ("Number" not in row) and ("Batting" not in row) and ("Totals" not in row) and ("Glossary" not in row) and ("" not in row):
                #create a new player
                offensive_stats = {}
                pitching_stats = {}
                defensive_stats = {}
                j = 0
                for i in range(3, 54, 1):
                    offensive_stats[offensive_stat_ids[j]] = row[i]
                    j += 1
                #print(offensive_stats)
                j = 0
                for z in range(55, 142, 1):
                    pitching_stats[pitching_stat_ids[j]] = row[z]
                    j += 1
                #print(pitching_stats)
                j = 0
                for k in range(143, 157, 1):
                    defensive_stats[defensive_stat_ids[j]] = row[k]
                    j += 1
                #print(defensive_stats)

                player = Player(row[2] + " " + row[1], None, offensive_stats, defensive_stats)
                players.append(player)

        # for player in players:
        #     print(player)

        return players







# Example usage
# read_csv('16u 2024 Midwestern Ontario Bearcats Summer 2024 Stats (1).csv')
