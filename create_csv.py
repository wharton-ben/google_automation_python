import csv

hosts = [["workstation.local", "192.168.1.1"], ["webserver.cloud", "10.1.1.1"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)