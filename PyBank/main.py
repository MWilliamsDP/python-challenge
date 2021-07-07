
   
# Import dependencies
import os
import csv

#define file path
filepath = "C:/Users/MW/Desktop/Homework/Python-Challenge/python-challenge/PyBank/Resources/budget_data.csv"

#name ariables
months = 0
TProfit = 0
ChangeinProfit = []
Average = []
MinDate = []
MaxDate = []
previousmonth = 0
 
#Open and Read file
with open (filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Pull and test header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #Count Months, total profit and find change
    for i in csvreader:
        months += 1
        TProfit += int (i[1])
        ChangeinProfit.append(int(i[1]) - previousmonth)
        previousmonth = int(i[1])

#Print inital results

print(f"CSV Header: {csv_header}")
print(f"Months: {months}")
print(f"Net total is {TProfit}")
print(f"Profit/Loss change: {ChangeinProfit}")

# sum
sum_PL_change = sum(ChangeinProfit)

# Find and print average change
Average = sum(ChangeinProfit)/len(ChangeinProfit)
print(f"The average change is {Average}")

# Find and print Greatest increase in profits
most_profit = max(ChangeinProfit)
print(f"the gratest increase in profits {most_profit}")

# Find and print Greatest decrease in profits
least_profit = min(ChangeinProfit)
print(f"The greatest decrease in profits is {least_profit}")

output_path = "C:/Users/MW/Desktop/Homework/Python-Challenge/python-challenge/PyBank/Analysis/Analysis.txt"

with open(output_path, "w") as txt:

    txt.write("Financial Analysis\n")

    txt.write("--------------------------------------------------\n")

    txt.write(f"Months: {months}")

    txt.write(f"Net total is {TProfit}")

    txt.write(f"The average change is {Average}")

    txt.write(f"the gratest increase in profits {most_profit}")

    txt.write (f"The greatest decrease in profits is {least_profit}")  