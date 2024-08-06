from Player import Player
import random

INNING = 0
OUTS = 0
HITTER = 0
BASES = [0, 0, 0, 0]  # [FIRST, SECOND, THIRD, HOME]
RUNS = 0


def advance_runners(hit: int):
    global BASES, RUNS
    new_bases = [0, 0, 0, 0]
    if hit == 1:
        for i in range(3):
            if BASES[i] == 1:
                # advance one base
                new_bases[i + 1] = 1
        new_bases[0] = 1  # batter to first
        if new_bases[3] == 1:
            # run scored
            RUNS += 1
    if hit == 2:
        for i in range(3):
            if BASES[i] == 1:
                if i != 2:
                    # advance two bases
                    new_bases[i + 2] = 1
                    if new_bases[3] == 1:
                        RUNS += 1
                        new_bases[3] = 0
                else:
                    # runner on third advances one bag
                    new_bases[3] = 1
                    RUNS += 1
        new_bases[1] = 1  # batter to second
    if hit == 3:
        # bases will clear
        # check for runs on base, all will score
        for i in range(3):
            if BASES[i] == 1:
                RUNS += 1
        new_bases[2] = 1
    if hit == 4:
        # bases will clear
        # check for runs on base, all will score
        for i in range(3):
            if BASES[i] == 1:
                RUNS += 1
        RUNS += 1  # for batter
        new_bases = [0, 0, 0, 0]
    BASES = new_bases

    print("NEW BASES: ")
    if BASES[0] == 1:
        print("RUNNER ON FIRST")
    if BASES[1] == 1:
        print("RUNNER ON SECOND")
    if BASES[2] == 1:
        print("RUNNER ON THIRD")




def gets_hit(p: Player):
    print(p.__str__())
    avg = p.offensive_stats.get('AVG')
    avg_as_int = int(avg.replace(".", ""))
    event = random.randint(0, 1000)
    if event < avg_as_int:
        return 1
    else:
        return 0


def is_extra_base_hit(p: Player):
    # Player has a hit at this point, need to figure out what kind

    num_hits = int(p.offensive_stats.get('H'))
    num_singles = int(p.offensive_stats.get('1B'))
    num_doubles = int(p.offensive_stats.get('2B'))
    num_triples = int(p.offensive_stats.get('3B'))
    num_homeruns = int(p.offensive_stats.get('HR'))

    single_cutoff = (num_singles / num_hits) * 1000
    double_cutoff = ((num_doubles / num_hits) * 1000) + single_cutoff
    triple_cutoff = ((num_triples / num_hits) * 1000) + double_cutoff
    homerun_cutoff = ((num_homeruns / num_hits) * 1000) + triple_cutoff

    #all probabilities add up to 1, or in this case 1000
    event = random.randint(0, 1000)

    if event <= single_cutoff:
        print("single")
        return 1
    elif single_cutoff < event <= double_cutoff:
        print("double")
        return 2
    elif double_cutoff < event <= triple_cutoff:
        print("triple")
        return 3
    else:
        print("homerun")
        return 4


def gets_on_base_conventional(p: Player):
    return 0


def gets_on_base_unconventional(p: Player):
    return 0


def run_sim(lineup: list):
    global INNING, OUTS, HITTER, RUNS, BASES
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
                advance_runners(is_extra_base_hit(lineup[HITTER]));
                HITTER += 1
                if HITTER == 9:
                    HITTER = 0
        OUTS = 0
        INNING += 1
        BASES = [0, 0, 0, 0]

    print("RUNS: ", RUNS)
    return 0
