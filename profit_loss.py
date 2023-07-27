from pathlib import Path
import csv
file_path= Path(r"c:\Users\cjiah\FJ3\profit&loss.csv")
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    profit_and_loss= []
    for row in reader:
        profit_and_loss.append(row[0], row[1], row[2], row[3], row[4])
print(profit_and_loss)