import profit_loss, cash_on_hand, overheads

def main():
    """
    """
    overhead_output = overheads.overhead()
    coh_output = cash_on_hand.cash()
    pnl_output = profit_loss.profit_n_loss()
    return overhead_output, coh_output, pnl_output
overhead_output, coh_output, pnl_output = main()

with open("summary_report.txt", "w") as file:
    file.write(f"{overhead_output}\n{coh_output}{pnl_output}")