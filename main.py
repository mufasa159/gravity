import random
from dataclasses import dataclass


@dataclass
class MFCount:
    active: int
    onsite: int
    remote: int


teachers = ["notebook", "universe", "canvas", "craft", "camera", "server", "spreadsheet", "blockchain", "influencer", "driver", "shop", "stage", "radio", "energy-drink"]
assistants = ["pen", "mind", "brush", "machine", "mic", "wifi", "clock", "etherum", "television", "passenger", "goods", "vision", "antenna", "headphones"]
week = ["mon", "tues", "wed", "thu", "fri"]

mf_data = [
    MFCount(11, 10, 1),
    MFCount(11, 10, 1),
    MFCount(17, 10, 7),
    MFCount(10, 5, 5),
    MFCount(10, 5, 5),
]

MAX_ONSITE = 17
MAX_REMOTE = 11

# capacity in each location
onsite_capacity = {
    "mb_bronx": 1,
    "mb_pville": 4,
    "lpa_casw": 2,
    "beca_hanac": 3,
    "ichs": 2,
    "fihs": 3,
    "wheels": 2
}

# first value is the capacity for mentors
mb_bronx = ["1"]
mb_pvile = ["4"]
lpa_casw = ["2"]
beca_hanac = ["3"]
ichs = ["2"]
fihs = ["3"]
wheels = ["2"]
remote = [str(MAX_REMOTE)]

day00 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day01 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day02 = [mb_bronx, mb_pvile, lpa_casw, beca_hanac]
day03 = [mb_bronx, mb_pvile]
day04 = [mb_bronx, mb_pvile]

this_week = [day00, day01, day02, day03, day04]


def print_array(title: str, array: list) -> None:
    print("------ " + title)
    for item in range(1, len(array)):
        print(array[item])


def generate_assignee(db: list) -> str:
    valid_user = False
    if len(db) == len(teachers)-1:
        user = random.choice(assistants)
    else:
        user = random.choice(teachers)

    while not valid_user:
        if user not in db:
            valid_user = True
        else:
            if len(db) < len(teachers):
                user = random.choice(teachers)
            else:
                user = random.choice(assistants)

    return user


for i in range(0, len(mf_data)):
    print("Day " + str(i + 1))

    assigned = []
    assigned_onsite = 0

    for person in range(0, mf_data[i].remote):
        to_be_assigned = generate_assignee(assigned)
        assigned.append(to_be_assigned)
        remote.append(to_be_assigned)

    while assigned_onsite != mf_data[i].onsite:
        for each_location in range(0, len(this_week[i])):
            for a in range(0, int(this_week[i][each_location][0])):
                to_be_assigned = generate_assignee(assigned)
                this_week[i][each_location].append(to_be_assigned)
                assigned.append(to_be_assigned)
                assigned_onsite += 1

    print_array("MB Bronx: ", mb_bronx)
    print_array("MB PVille: ", mb_pvile)
    print_array("LPA / Casw: ", lpa_casw)
    print_array("Beca / Hanac: ", beca_hanac)
    print_array("ICHS: ", ichs)
    print_array("FIHS: ", fihs)
    print_array("WHEELS: ", wheels)
    print_array("Remote: ", remote)
    print("\n")

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

