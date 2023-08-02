from pathlib import Path
import csv

def profit_and_loss():
    """
    - Calculates and finds profit deficit or surplus, and gives the highest value and day it occured
    - No parameters needed
    """
    file_path= Path(r"c:\Users\Public\FJ3\csv_reports\profit&loss.csv")
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        profit_and_loss= []
        for row in reader:
            profit_and_loss.append([row[0], row[1], row[2], row[3], float(row[4])])

    profit_difference = [profit_and_loss[i][4] - profit_and_loss[i-1][4] for i in range(1, len(profit_and_loss))]

    profit_deficit = [value for value in profit_difference if value < 0]
    profit_surplus = [value for value in profit_difference if value > 0]

    if profit_deficit:
        for deficit in profit_deficit:
            deficit_index = profit_difference.index(deficit)
            deficit_day = profit_and_loss[deficit_index + 1][0]
            print(f"[PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{abs(deficit)}")
    else:
        for surplus in profit_surplus:
            highest_surplus = max(profit_surplus)
            highest_surplus_index = profit_surplus.index(highest_surplus)
            highest_surplus_day = profit_and_loss[highest_surplus_index + 1][0]
        print(f" [NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY \n [HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day}, AMOUNT: {highest_surplus}")
profit_and_loss()