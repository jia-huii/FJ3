def profit_n_loss():
    """
    - Calculates and finds profit deficit or surplus, and gives the highest value and day it occured
    - No parameters needed
    """
    from pathlib import Path
    import csv
    # define the file path
    file_path= Path(r"c:\Users\Public\FJ3\csv_reports\profit&loss.csv")

    # Open and read the CSV file
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        # Create an empty list, profit_and_loss and append CSV information into it
        profit_and_loss= []
        for row in reader:
            profit_and_loss.append([row[0], row[1], row[2], row[3], float(row[4])])

    # Calculate the difference in profit between consecutive days
    profit_difference = [profit_and_loss[i][4] - profit_and_loss[i-1][4] for i in range(1, len(profit_and_loss))]

    # Separate deficit and surplus values
    profit_deficit = [value for value in profit_difference if value < 0]
    profit_surplus = [value for value in profit_difference if value > 0]

    # Initialize the output string
    output = ""
    # If there is profit deficit, code will give deficit amount and respective days
    # If there is only profit surplus, code will give highest surplus amount and respective day
    if profit_deficit:
        for deficit in profit_deficit:
            deficit_index = profit_difference.index(deficit)
            deficit_day = profit_and_loss[deficit_index + 1][0]
            output += f"[PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{abs(deficit)}\n"
    else:
        for surplus in profit_surplus:
            highest_surplus = max(surplus)
            highest_surplus_index = profit_surplus.index(highest_surplus)
            highest_surplus_day = profit_and_loss[highest_surplus_index + 1][0]
            output += f" [NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY \n [HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day}, AMOUNT: {highest_surplus}"
    # Return the final output string
    return output