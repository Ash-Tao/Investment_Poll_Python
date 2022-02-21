
# import the os module, will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

ProfitLosses = []
change = []
totalline = 0
lastProfitLosses = 0

# create file path
csvpath = os.path.join('Resources','budget_data.csv')
# open the file
with open(csvpath) as csvfile:
    # read the csv file by delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')
    # stores the header row
    csv_header = next(csvreader)
    # use loop to get the list of "Profit/Losses", "total months" and "average change"
    for row in csvreader:
        # list of "Profit/Losses"
        ProfitLosses.append(int(row[1]))
        # Total Months
        totalline = totalline + 1
        # Total changes
        # The first result, need will be exclusive in the following steps, since the change only starts from the second record. (-354534(Feb-10) - 1088983(Jan-10))
        # Average Change = total changes / total months
        change.append(int(row[1]) - lastProfitLosses)
        # find the month of the greatest increase in profits
        if lastProfitLosses != 0:
            if (int(row[1]) - lastProfitLosses) == max(change):
                maxmonth = row[0]
            if (int(row[1]) - lastProfitLosses) == min(change):
                minmonth = row[0]
        # This code will be executed first and only once in the loop.
        # Even though it is written after others. 
        # Because the first lastProfitLosses is set =0 and will be given a new non-0 value at the end of each loop.
        else:
            # Exclusive the first result. (1088983(Jan-10) - 0 (no data))
            change.pop(0)
        # Set ProfitLosses as lastProfitLosses for  next loop calculation
        lastProfitLosses=int(row[1])

# make the calculation
totalmonths = f"Total Months: {totalline}"
totalPL = f"Total: ${sum(ProfitLosses)}"
averagechange = f'Average Change: ${"{:.2f}".format(sum(change)/(totalline-1))}'
greatestinPL = f"Greatest Increase in Profits: {maxmonth} (${max(change)})"
greatestdePL = f"Greatest Decrease in Profits: {minmonth} (${min(change)})"
# make a list for the output.
completelist = (" ","Financial Analysis","-----------------------------------",totalmonths,totalPL,averagechange,greatestinPL,greatestdePL)

# use loop show the output list in the Terminal
for output in completelist:
    print(output)


# create file and its path
output_file = os.path.join('analysis','output.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w") as datafile:
    # use loop save the output list in the .txt file
    for output in completelist:
        datafile.writelines(output)
        datafile.writelines("\n")



    
