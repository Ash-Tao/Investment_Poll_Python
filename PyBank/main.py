

import os
import csv

ProfitLosses = []
change = []
totalline = 0
lastPL = 0

csvpath = os.path.join('/Users','ash.tao','python-challenge','PyBank','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        ProfitLosses.append(int(row[1]))
        totalline = totalline + 1
        change.append(int(row[1]) - lastPL)
        if lastPL != 0:
            if (int(row[1]) - lastPL) == max(change):
                maxmonth = row[0]
                #print(maxmonth)
            if (int(row[1]) - lastPL) == min(change):
                minmonth = row[0]
                #print(minmonth)
        else:
            change.pop(0)
        lastPL=int(row[1])


totalmonths = f"Total Months: {totalline}"
totalPL = f"Total: ${sum(ProfitLosses)}"
averagechange = f'Average Change: ${"{:.2f}".format(sum(change)/(totalline-1))}'
greatestinPL = f"Greatest Increase in Profits: {maxmonth} (${max(change)})"
greatestdePL = f"Greatest Decrease in Profits: {minmonth} (${min(change)})"

outputs = (" ","Financial Analysis","-----------------------------------",totalmonths,totalPL,averagechange,greatestinPL,greatestdePL)

for output in outputs:
    print(output)

output_file = os.path.join('/Users','ash.tao','python-challenge','PyBank','analysis','output.txt')
with open(output_file, "w") as datafile:
    for output in outputs:
        datafile.writelines(output)
        datafile.writelines("\n")



    
