from pathlib import Path
import csv
file_path= Path(r"c:\Users\cjiah\FJ3\csv_reports\profit&loss.csv")
# print(file_path.exists())
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    profit_and_loss= []
    for row in reader:
        profit_and_loss.append([row[0], row[1], row[2], row[3], float(row[4])])
print(profit_and_loss)

profit_difference = [profit_and_loss[i][4] - profit_and_loss[i-1][4] for i in range(1, len(profit_and_loss))]
print(profit_difference)