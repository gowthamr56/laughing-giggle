import os
import datetime

today = str(datetime.datetime.today()) + "\n"
print(today)

with open("log.txt", "a") as file:
    file.write(today)

print("log file updated")
