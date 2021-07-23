import csv

users = [ {"name": "Ben", "username": "Ben123", "department": "IT"}, 
        {"name": "Jerry", "username": "Jerry123", "department": "Network"}, 
        {"name": "Tim", "username": "Tim123", "department": "Software"}, ]


keys = ["name","username","department"]
with open('users_by_dept.csv', 'w') as users_by_dept:
    writer = csv.DictWriter(users_by_dept, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
