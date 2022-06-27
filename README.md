## Gravity

Made to simplify assigning specific members to different locations randomly.

**Why is it named Gravity?**  
Well, it felt like this whole scheduling thing for the summer is the "glue" to hold everything together...

---

### Data
All necessary data for running the script is stored in the `./data` directory. Make sure the format matches when adding new information to any of the csv files.

| Filename | Description |  
| -------- | ----------- |
| `worksites.csv` | Locations to assign members to and max capacity for mentors/facilitators|  
| `mentors.csv` | List of mentors and their locality |
| `facilitators.csv` | List of facilitators and their locality |
| `schools.csv` | List of schools/programs, number of participants and the amount of mentors/facilitators needed for each
| `daily.csv` | Most important file. It contains lists of which school/program will be present each day. The script automatically calculates how many mentors/facilitaors will be online and remote based on this information |

### Backlog
- consider mentors' and facilitators' locations (there's a Queens borough outlier)
- add occurrence counter
- track budget if time permits
- add a way to track the number of times a person is assigned to a location