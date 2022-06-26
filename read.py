from custom_dataclass import *


def people(filename: str) -> list[Person]:
    """
    Reads the file and returns a list of Person objects.
    :param filename: String
    :return: List of `Person` objects
    """
    all_people = []
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
            if count > 1:
                line = line.strip()
                if line:
                    try:
                        name, location = line.split(',')
                        all_people.append(Person(name, location))
                    except:
                        print("Invalid data : read.people()")
    return all_people


def worksites(filename_a: str) -> list[Worksite]:
    """
    Reads the file and returns a list of Worksite objects.
    :param filename_a: String
    :return: list of `Worksite` objects
    """
    all_worksites = []
    count = 0
    with open(filename_a, encoding='utf-8') as f:
        for line in f:
            count += 1
            if count > 1:
                line = line.strip()
                if line:
                    fields = line.split(',')
                    try:
                        name = fields[0]
                        occupants = fields[1].split(' ')
                        mf_capacity = int(fields[2])
                        all_worksites.append(Worksite(name, occupants, int(mf_capacity)))
                    except:
                        print("Invalid data : read.worksites()")
                        exit(1)
    return all_worksites


def school(filename: str) -> list[dict[str, int]]:
    """
    Reads the file and returns a list of dictionaries.
    :param filename: String
    :return: List of dictionaries `dict[school_name, mf_count]`
    """
    all_schools = []
    each_school = dict()
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
            if count > 1:
                line = line.strip()
                if line:
                    fields = line.split(',')
                    try:
                        name = fields[0]
                        mf_count = int(fields[2])
                        each_school[name] = mf_count
                        all_schools.append(each_school)
                    except:
                        print("Invalid data : read.school()")
                        exit(1)
    return all_schools


def daily_active(filename_count: str, all_worksites: list[Worksite], all_schools: list) -> list[DailyActive]:
    """
    Reads the file and returns a list of `DailyActive` objects.
    :param filename_count: String
    :param all_worksites: List of `Worksite` objects
    :param all_schools: List of dictionaries `dict[school_name, mf_count]`
    :return: List of `DailyActive` objects
    """
    result = []                 # stores DailyActive values to return upon call
    worksite_active = []        # stores Worksite values for each worksite
    worksite_capacity = dict()
    count = 0
    with open(filename_count, encoding='utf-8') as f:
        for line in f:
            count += 1
            if count > 1:
                line = line.strip()             # separate each line
                if line:
                    try:
                        fields = line.split(',')
                        day = int(fields[0])
                        schools = fields[1].split(" ")
                        mf_active, mf_onsite, mf_remote = 0, 0, 0

                        for i in range(0, len(schools)):

                            # list active workplaces per day
                            for j in range(0, len(all_worksites)):
                                worksite_capacity[all_worksites[j].name] = all_worksites[j].mf_capacity
                                if schools[i] in all_worksites[j].occupants:
                                    worksite_active.append(all_worksites[j])

                            # only store unique worksite names per day in `place_per_day` list
                            places_per_day = []
                            for k in range(0, len(worksite_active)):
                                if not worksite_active[k].name in places_per_day:
                                    places_per_day.append(worksite_active[k].name)

                            # count active mentors and facilitators per day
                            if schools[i] != "N/A":
                                mf_active += all_schools[i][schools[i]]

                        # count onsite mentors and facilitators per day
                        for y in range(0, len(places_per_day)):
                            if places_per_day[y] != 'Remote':
                                mf_onsite += worksite_capacity[places_per_day[y]]

                        # count remote mentors and facilitators per day
                        mf_remote = mf_active - mf_onsite
                        if mf_remote < 0:
                            mf_onsite += mf_remote
                            mf_remote = mf_active - mf_onsite

                        result.append(DailyActive(day, places_per_day, mf_active, mf_onsite, mf_remote))
                        del worksite_active[:]
                    except:
                        print("Invalid data : read.daily_active()")
                        exit(1)
    return result
