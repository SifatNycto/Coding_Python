import csv

with open("infobook.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "id"])

    if file.tell() == 0:
        writer.writeheader()

    name = input("Name: ")
    id = input("ID: ")

    writer.writerow({"name": name, "id": id})
