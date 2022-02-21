# Python-Challenge
## Purpose
Creating Python scripts to analyze the records on the given `.csv` datasets.<br />
> *- Both challenges require locateing and reading a source file.*<br />
> *- Need to create a new file for the final report and save it, while display the results in the terminal after completed analysis.*<br />
> *- The first two steps and the last step are the same for each scripts.*<br />

- import os module to get the file path and be able to read, write and save the file.
  ``` Python
  import os
  csvpath = os.path.join('Resources','###.csv')
  ```
- import csv module to read the `.csv` file.
  ``` Python
  import csv
  with open(csvpath) as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       csv_header = next(csvreader)
  ```
- Make the calculation based on the difference request
  - PyBank
  - PyPoll
- use loops for displaying it in terminal, creating and saving the files.<br />
  ``` Python
  for output in completelist:
      print(output)
      
  output_file = os.path.join('analysis','Analysis Results.txt')
  with open(output_file, "w") as datafile:
       for output in completelist:
           datafile.writelines(output)
           datafile.writelines("\n")
  ```
--- 

## PyBank
### Target
The given dataset is composed of two columns: "Date" and "Profit/Losses".<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/PyBank%20Resources%20Datasets%20.png)<br />
Final Exported Repoet:<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/Results%20for%20PyBank.png)<br />

### The way to approach
> *It is divided into two parts:*<br />
- Use loop to find the value.<br />
  ``` python
  for row in csvreader:
  ```
  - The total number of months.
    ``` python
    totalline = totalline + 1
    ```
  - The net total amount of "Profit/Losses" over the entire period
    ``` Python
    ProfitLosses.append(int(row[1]))
    totalPL = f"Total: ${sum(ProfitLosses)}"
    ```
  - The changes in "Profit/Losses" over the entire period, and then the average of those changes.
    ``` Python
    change.append(int(row[1]) - lastProfitLosses)
    if lastProfitLosses != 0:
        if (int(row[1]) - lastProfitLosses) == max(change):
            maxmonth = row[0]
        if (int(row[1]) - lastProfitLosses) == min(change):
            minmonth = row[0]
    else:
        change.pop(0)
    lastProfitLosses=int(row[1])
    ```
  ``` Python
  averagechange = f'Average Change: ${"{:.2f}".format(sum(change)/(totalline-1))}'
  ```
  - The greatest increase in profits (date and amount) over the entire period.
  ``` Python
  greatestinPL = f"Greatest Increase in Profits: {maxmonth} (${max(change)})"
  ```
  - The greatest decrease in profits (date and amount) over the entire period.
  ``` Python
  greatestdePL = f"Greatest Decrease in Profits: {minmonth} (${min(change)})"
  ```
- Combine values into a list<br />
  ``` Python
  completelist = (" ","Financial Analysis","-----------------------------------",totalmonths,totalPL,averagechange,greatestinPL,greatestdePL)
  ```
---

## PyPoll
The given dataset is composed of three columns: "Voter ID", "County", and "Candidate".<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/PyPoll%20Resources%20Datasets%20.png)<br />
Final Exported Repoet:<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/Results%20for%20PyPoll.png)<br />
### The way to approach
- The total number of votes cast.
  ``` Python
  votesdetails = []
  totalvotes = 0
  for row in csvreader:
      totalvotes = totalvotes + 1
      votesdetails.append(row[2])   
    ```
- And a complete list of candidates who received votes
  ``` python
  candidate = []
  candidate = list(dict.fromkeys(votesdetails))
  ```
- The total number and percentage of votes each candidate won.
  ``` python
  voteresult = []
  for x in candidate:
      voteresult.append(votesdetails.count(x))
      eachcandidate = voteresult[candidate.index(x)]
      eachcandidatepercent = "{:.3%}".format(eachcandidate/totalvotes)
- The winner of the election based on popular vote.
  ``` Python
  candidate[voteresult.index(max(voteresult))]
  ```
## How to Run
- Download two files.
  - [PyBank](https://github.com/Ash-Tao/python-challenge/tree/main/PyBank)<br />
  - [PyPoll](https://github.com/Ash-Tao/python-challenge/tree/main/PyPoll)<br />
- Run the `main.py` in termminal
- Go to the subfolder `analysis`, you will find a `Analysis Results.txt` for the final report.
