CURRENT_LINEUP_RUNS_PER_GAME = []
CURRENT_LINEUP = []
TOP_RUNS_PER_GAME = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TOP_LINEUPS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def update_current_run(runs, lineup):
    global CURRENT_LINEUP_RUNS_PER_GAME, CURRENT_LINEUP

    CURRENT_LINEUP_RUNS_PER_GAME.append(runs)
    CURRENT_LINEUP = lineup
    # print(CURRENT_LINEUP)
    # print(CURRENT_LINEUP_RUNS_PER_GAME)

def update_rankings():
    global CURRENT_LINEUP, CURRENT_LINEUP_RUNS_PER_GAME
    avg_runs = 0
    for i in range(10):
        avg_runs += CURRENT_LINEUP_RUNS_PER_GAME[i]

    avg_runs = avg_runs / 10

    for j in range(10):
        if avg_runs > TOP_RUNS_PER_GAME[j]:
            TOP_RUNS_PER_GAME[j] = avg_runs
            TOP_LINEUPS[j] = CURRENT_LINEUP
            break
    CURRENT_LINEUP_RUNS_PER_GAME = []
    CURRENT_LINEUP = []
