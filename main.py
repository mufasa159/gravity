# Originally created on June 22, 2022
# By @mufasa159
# For @metabronx
# To make assigning people to different locations easier

from custom_dataclass import *
import random
import read

# read data from csv files
mentors = read.people("./data/mentors.csv")
facilitators = read.people("./data/facilitators.csv")
worksite_list = read.worksites("data/worksites.csv")
school_list = read.school("data/schools.csv")
daily_data = read.daily_active("data/daily.csv", worksite_list, school_list)

# store worksite data in a dictionary for convenient access
mf_capacity_per_location = []
worksite_dictionary = {}
for q in range(0, len(worksite_list)):
    worksite_dictionary[worksite_list[q].name] = worksite_list[q].mf_capacity


def print_array(title: str, array: list) -> None:
    print("\n# " + title)
    for item in range(1, len(array)):
        print(array[item])


def generate_person(verification_list: list) -> Person:
    """
    Generates a random person from the verification list.
    Prioritized mentors since they are more likely to work in-person.
    :param verification_list: List
    :return: `Person` object
    """
    valid_user = False
    if len(verification_list) < len(mentors):
        user = random.choice(mentors)
    else:
        user = random.choice(facilitators)

    while not valid_user:
        if user not in verification_list:
            valid_user = True
        else:
            if len(verification_list) < len(mentors):
                user = random.choice(mentors)
            else:
                user = random.choice(facilitators)

    return user


# main loop that assigns people to different locations
for i in range(0, len(daily_data)):
    print("\nDay " + str(daily_data[i].day))

    assigned = []
    people_per_location_dict = {}  # stores list of names per location

    for each_location_index in range(0, len(daily_data[i].workplace)):
        if daily_data[i].workplace[each_location_index] != "Remote":
            temp = []
            for each_mf_capacity in range(0, worksite_dictionary[daily_data[i].workplace[each_location_index]]):
                to_be_assigned = generate_person(assigned)
                assigned.append(to_be_assigned)
                temp.append(to_be_assigned.name)
                people_per_location_dict[daily_data[i].workplace[each_location_index]] = temp

    # loop repeat separately so that mentors get more priority in being assigned in-person than facilitators
    for each_location_index in range(0, len(daily_data[i].workplace)):
        if daily_data[i].workplace[each_location_index] == "Remote":
            temp = []
            for each_mf_capacity in range(0, daily_data[i].placement.remote):
                to_be_assigned = generate_person(assigned)
                assigned.append(to_be_assigned)
                temp.append(to_be_assigned.name)
                people_per_location_dict[daily_data[i].workplace[each_location_index]] = temp

    for x in range(0, len(people_per_location_dict)):
        print(str(daily_data[i].workplace[x]) + ": " + str(people_per_location_dict[daily_data[i].workplace[x]]))
