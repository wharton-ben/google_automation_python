import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users and is on version number {}").format(row["name"], row["users"], row["version"]))