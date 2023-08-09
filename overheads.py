def overhead():
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

    total_amount = sum(item[1] for item in overheads)

    total_marketing = 0
    total_salary = 0
    total_rental = 0
    total_shipping = 0
    total_depreciation = 0
    total_interest = 0
    total_penalty = 0
    total_HR = 0
    total_maintenance = 0
    overflow_retail = 0
    overflow_warehouse = 0
    total_oveflow = 0

    for item in overheads:
        if item[0] == "Marketing Expense":
            total_marketing += item[1]
        if item[0] == "Salary Expense":
            total_salary += item[1]
        if item[0] == "Rental Expense":
            total_rental += item[1]
        if item[0] == "Shipping Expense":
            total_shipping += item[1]
        if item[0] == "Depreciation Expense":
            total_depreciation += item[1]
        if item[0] == "Interest Expense ":
            total_interest += item[1]
        if item[0] == "Penalty Expense":
            total_penalty += item[1]
        if item[0] == "Human Resource Expense":
            total_HR += item[1]
        if item[0] == "Maintenance Expense":
            total_maintenance += item[1]
        if item[0] == "Overflow Expense - Retail":
            overflow_retail += item[1]
        if item[0] == "Overflow Expense - Warehouse":
            overflow_warehouse += item[1]
        total_oveflow = overflow_retail + overflow_warehouse

    marketing_percent = round((total_marketing/ total_amount) * 100, 2)
    salary_percent = round((total_salary/ total_amount) * 100, 2)
    rental_percent = round((total_rental/ total_amount) * 100, 2)
    shipping_percent = round((total_shipping/ total_amount) * 100, 2)
    depreciation_percent = round((total_depreciation/ total_amount) * 100, 2)
    interest_percent = round((total_interest/ total_amount) * 100, 2)
    penalty_percent = round((total_penalty/ total_amount) * 100, 2)
    HR_percent = round((total_HR/ total_amount) * 100, 2)
    maintenance_percent = round((total_maintenance/ total_amount) * 100, 2)
    overflow_percent = round((total_oveflow/ total_amount) * 100, 2)

    overhead_type = ["MARKETING EXPENSE", "SALARY EXPENSE", "RENTAL EXPENSE", "SHIPPING EXPENSE", "DEPRECIATION EXPENSE", "INTEREST EXPENSE", "PENALTY EXPENSE", "HUMAN RESOURCE EXPENSE", "OVERFLOW EXPENSE"]
    percentages = [marketing_percent, salary_percent, rental_percent, shipping_percent, depreciation_percent, interest_percent, penalty_percent, HR_percent, maintenance_percent, overflow_percent]
    highest_percent = max(percentages)
    highest_indexes = [i for i, percent in enumerate(percentages) if percent == highest_percent]
    highest_overhead = [overhead_type[i] for i in highest_indexes]
    return f"[HIGHEST OVERHEAD] {', '.join(highest_overhead)}: {highest_percent}%"