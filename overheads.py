from pathlib import Path
import csv

file_path= Path(r"c:\Users\Public\FJ3\csv_reports\overheads.csv")
# print(file_path.exists())
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    overheads= []
    for row in reader:
        overheads.append([row[1], float(row[3])])
# print(overheads)

total = [overheads[i][1] + overheads[i-1][1] for i in range(1, len(overheads))]
print(total)