import profit_loss
import cash_on_hand
import overheads


from pathlib import Path

home = Path.home()
# create a file path for summary_report.txt
file_path= Path(r"C:\Users\Public\FJ3\summary_report.txt")
file_path.touch()
print(file_path.exists())
# use mode= "w" to write data to summary_report.txt file
with file_path.open(mode= "w", encoding= "UTF-8") as file:
    # Write the output of each function to the file
    file.writelines(f"{profit_loss.profit_n_loss()}\n {cash_on_hand.cash()}\n {overheads.overhead()}")