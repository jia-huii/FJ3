import profit_loss, cash_on_hand, overheads

def main():
    """
    - Combines cash, profit_n_loss and overhead function into one function
    - No parameters needed
    """
    # Call the overheads function to get overhead information
    overhead_output = overheads.overhead()

    # Call the cash_on_hand function to get cash deficit/surplus information
    coh_output = cash_on_hand.cash()

    # Call the profit_loss function to get profit deficit/surplus information
    pnl_output = profit_loss.profit_n_loss()

    # Return the outputs from each function
    return overhead_output, coh_output, pnl_output

# Call the main function to get the outputs
overhead_output, coh_output, pnl_output = main()

# Write the outputs to a summary report file
with open("summary_report.txt", "w") as file:
    file.write(f"{overhead_output}\n{coh_output}{pnl_output}")