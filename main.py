# Originally created on June 22, 2022
# By @mufasa159
# For @metabronx
# To make assigning people to different locations easier

import random
from dataclasses import dataclass


@dataclass
class MFCount:
    active: int
    onsite: int
    remote: int


mentors = ["notebook", "universe", "canvas", "craft", "camera", "server", "spreadsheet", "blockchain", "influencer", "driver", "shop", "stage", "radio", "energy-drink"]
facilitators = ["pen", "mind", "brush", "machine", "mic", "wifi", "clock", "etherum", "television", "passenger", "goods", "vision", "antenna", "headphones"]
week = ["mon", "tues", "wed", "thu", "fri"]

mf_data = [
    MFCount(11, 10, 1),
    MFCount(11, 10, 1),
    MFCount(17, 10, 7),
    MFCount(10, 5, 5),

    MFCount(10, 5, 5),
    MFCount(17, 10, 7),
    MFCount(17, 10, 7),
    MFCount(17, 10, 7),
    MFCount(10, 5, 5),

    MFCount(18, 10, 8),
    MFCount(25, 15, 10),
    MFCount(25, 15, 10),
    MFCount(25, 15, 10),
    MFCount(10, 5, 5),

    MFCount(21, 12, 9),
    MFCount(28, 17, 11),
    MFCount(28, 17, 11),
    MFCount(28, 17, 11),
    MFCount(10, 5, 5),
]

# first value is the onsite capacity for mentors and facilitators
mb_bronx = ["1"]
mb_pvile = ["4"]
lpa_casw = ["2"]
beca_hanac = ["3"]
ichs = ["2"]
fihs = ["3"]
wheels = ["2"]
remote = ["11"]

day01 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day02 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day03 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day04 = [mb_bronx, mb_pvile]

day05 = [mb_bronx, mb_pvile]
day06 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day07 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day08 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day09 = [mb_bronx, mb_pvile]

day10 = [mb_bronx, mb_pvile, fihs, wheels]
day11 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels]
day12 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels]
day13 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels]
day14 = [mb_bronx, mb_pvile]

day15 = [mb_bronx, mb_pvile, fihs, wheels, ichs]
day16 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels, ichs]
day17 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels, ichs]
day18 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac, fihs, wheels, ichs]
day19 = [mb_bronx, mb_pvile]

this_week = [day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11, day12, day13, day14, day15, day16, day17, day18, day19]


def print_array(title: str, array: list) -> None:
    print("\n# " + title)
    for item in range(1, len(array)):
        print(array[item])


def generate_assignee(db: list) -> str:
    valid_user = False
    if len(db) < len(mentors):
        user = random.choice(mentors)
    else:
        user = random.choice(facilitators)

    while not valid_user:
        if user not in db:
            valid_user = True
        else:
            if len(db) < len(mentors):
                user = random.choice(mentors)
            else:
                user = random.choice(facilitators)

    return user


for i in range(0, len(mf_data)):
    print("Day " + str(i + 1))

    assigned = []
    assigned_onsite = 0

    while assigned_onsite != mf_data[i].onsite:
        for each_location in range(0, len(this_week[i])):
            for a in range(0, int(this_week[i][each_location][0])):
                to_be_assigned = generate_assignee(assigned)
                this_week[i][each_location].append(to_be_assigned)
                assigned.append(to_be_assigned)
                assigned_onsite += 1

    for person in range(0, mf_data[i].remote):
        to_be_assigned = generate_assignee(assigned)
        assigned.append(to_be_assigned)
        remote.append(to_be_assigned)

    print_array("MB Bronx: ", mb_bronx)
    print_array("MB PVille: ", mb_pvile)
    print_array("LPA/Casw: ", lpa_casw)
    print_array("Beca/Hanac: ", beca_hanac)
    print_array("ICHS: ", ichs)
    print_array("FIHS: ", fihs)
    print_array("WHEELS: ", wheels)
    print_array("Remote: ", remote)
    print("\n________________________________________\n")

    del assigned[:]
    del mb_bronx[1:]
    del mb_pvile[1:]
    del lpa_casw[1:]
    del beca_hanac[1:]
    del ichs[1:]
    del fihs[1:]
    del wheels[1:]
    del remote[1:]
    assigned_onsite -= assigned_onsite

