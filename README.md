# Python-Challenge
- Creating Python scripts to analyze the records on the given `.csv` datasets.<br />
  - import os module to get the file path and be able to read, write and save the file.
    ``` Python
    # import the os module, will allow us to create file paths across operating systems
    import os
    # create file path
    csvpath = os.path.join('Resources','election_data.csv')

      ```
  - import csv module to read the `.csv` file.
    ``` Python
    # Module for reading CSV files
    import csv
    # open the file
    with open(csvpath) as csvfile:
         # read the csv file by delimiter and variable
         csvreader = csv.reader(csvfile, delimiter=',')
         # stores the header row
         csv_header = next(csvreader)
    ```
  - The final script should both print the analysis to the terminal and export a text file with the results.<br />
  
     > *Both python scripts need to generate a `.txt` files while displaying the results in the terminal, and save the `.txt` files in a local folder. Therefore, at the end of coding, I set the results as a list, and use loops to display, create and save the files.*<br />
     ``` Python
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
     ```
--- 

## PyBank
### Target
The given dataset is composed of two columns: "Date" and "Profit/Losses".<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/PyBank%20Resources%20Datasets%20.png)<br />
Your analysis should look similar to the following:<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/Results%20for%20PyBank.png)<br />

### The way to approach
- The total number of months.
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in profits (date and amount) over the entire period.
---

## PyPoll
The given dataset is composed of three columns: "Voter ID", "County", and "Candidate".<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/PyPoll%20Resources%20Datasets%20.png)<br />
Your analysis should look similar to the following:<br />
![alt text](https://github.com/Ash-Tao/python-challenge/blob/main/Image/Results%20for%20PyPoll.png)<br />
### The way to approach
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

## How to Run
- 
## Files
