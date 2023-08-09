def cash():
    """
    - Calculates and finds cash deficit or surplus, and gives the highest value and day it occured
    - No parameters needed
    """
    from pathlib import Path
    import csv

    # define the file path
    file_path= Path(r"c:\Users\Public\FJ3\csv_reports\cash_on_hand.csv")

    # Open and read the CSV file
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        # Create an empty list, cash_on_hand and append CSV information into it
        cash_on_hand= []
        for row in reader:
            cash_on_hand.append([row[0], float(row[1])])

    # Calculate the difference in cash between consecutive days
    cash_difference = [cash_on_hand[i][1] - cash_on_hand[i - 1][1] for i in range(1, len(cash_on_hand))]

    # Separate deficit and surplus values
    cash_deficit = [value for value in cash_difference if value < 0]
    cash_surplus = [value for value in cash_difference if value > 0]

    # Initialize the output string
    output = ""
    # If there is cash deficit, code will give deficit amount and respective days
    # If there is only cash surplus, code will give highest surplus amount and respective day
    if cash_deficit:
        for deficit in cash_deficit:
            deficit_index = cash_difference.index(deficit)
            deficit_day = cash_on_hand[deficit_index + 1][0]
            output += f"[CASH DEFICIT] DAY: {deficit_day}, AMOUNT: USD{abs(deficit)}\n"
    else:
        for surplus in cash_surplus:
            highest_surplus = max(cash_surplus)
            highest_surplus_index = cash_surplus.index(highest_surplus)
            highest_surplus_day = cash_on_hand[highest_surplus_index + 1][0]
            output += f" [CASH SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY \n [HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: {highest_surplus}"
    # Return the final output string
    return output