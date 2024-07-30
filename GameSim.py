from Player import Player
import random

INNING = 0
OUTS = 0
HITTER = 0

def gets_hit(p: Player):
    print(p.__str__())
    avg = p.offensive_stats.get('AVG')
    avg_as_int = int(avg.replace(".", ""))
    event = random.randint(0, 1000)
    print("EVENT: ", event)
    print("AVG: ", avg_as_int)
    if event <= avg_as_int:
        return 1
    else:
        return 0


def gets_on_base_conventional(p: Player):
    return 0


def gets_on_base_unconventional(p: Player):
    return 0
def run_sim(lineup: list):
    global INNING, OUTS, HITTER
    while INNING < 7:
        while OUTS < 3:
            if gets_hit(lineup[HITTER]) == 0:
                if gets_on_base_conventional(lineup[HITTER]) == 0:
                    if gets_on_base_unconventional(lineup[HITTER]) == 0:
                        print("out")
                        OUTS += 1
                        HITTER += 1
                        if HITTER == 9:
                            HITTER = 0
            else:
                print("hit")
                HITTER += 1
                if HITTER == 9:
                    HITTER = 0
        OUTS = 0
        INNING += 1
    return 0



