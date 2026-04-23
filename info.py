import csv

# with open("info.csv", "a") as file:
#     name = input("Name: ")
#     ID = input("ID: ")
    
#     write = csv.writer(file)
#     write.writerow([name, ID])


file = open("info.csv", "a")

name = input("Name: ")
ID = input("ID: ")

write = csv.writer(file)
write.writerow([name, ID])

file.close()