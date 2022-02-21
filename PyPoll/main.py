# import the os module, will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

votesdetails = []
candidate = []
totalvotes = 0

# create file path
csvpath = os.path.join('Resources','election_data.csv')
# open the file
with open(csvpath) as csvfile:
    # read the csv file by delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')
    # stores the header row
    csv_header = next(csvreader)
    for row in csvreader:
        # have the list of all the votes
        votesdetails.append(row[2])
        # have the total amount of votes
        totalvotes = totalvotes + 1
# have the list of 3 candidates by removing the duplicated name from the he list of all the votes
candidate = list(dict.fromkeys(votesdetails))
print(candidate)
voteresult = []
winner = []
# create the top part of the output list 
toplist = [' ','Election Results','-------------------------',f'Total Votes: {totalvotes}','-------------------------']
completelist = []
# create the second part of the output list 
for x in candidate:
    # have the list of total amount of each candidate
    voteresult.append(votesdetails.count(x))
    # total votes amount of each candidate
    eachcandidate = voteresult[candidate.index(x)]
    # percentage of votes amount of each candidate
    eachcandidatepercent = "{:.3%}".format(eachcandidate/totalvotes)
    # combine top part and the second part of the output list
    toplist.append(f'{x}: {eachcandidatepercent} ({eachcandidate})')
# create the last part of the output list 
# find the max votes amount in the list - voteresult.
# use index find the name in list - candidate, which is related to the above maximum value 
winner = ['-------------------------',f'Winner: {candidate[voteresult.index(max(voteresult))]}','-------------------------']
# combine the last part of the output list
completelist = toplist + winner

# use loop show the output list in the Terminal
for output in completelist:
    print(output)

# create file and its path
output_file = os.path.join('analysis','Analysis Results.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w") as datafile:
    # use loop save the output list in the .txt file
    for output in completelist:
        datafile.writelines(output)
        datafile.writelines("\n")
