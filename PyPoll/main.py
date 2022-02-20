import os
import csv
from traceback import print_tb

votesdetails = []
candidate = []
totalvotes = 0
csvpath = os.path.join('/Users','ash.tao','Desktop','PyPoll','Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        votesdetails.append(row[2])
        totalvotes = totalvotes + 1


candidate = list(dict.fromkeys(votesdetails))
voteresult = []
winner = []
toplist = [' ','Election Results','-------------------------',f'Total Votes: {totalvotes}','-------------------------']
completelist = []
for x in candidate:
    voteresult.append(votesdetails.count(x))
    eachcandidate = voteresult[candidate.index(x)]
    eachcandidatepercent = "{:.3%}".format(eachcandidate/totalvotes)
    toplist.append(f'{x}: {eachcandidatepercent} ({eachcandidate})')
winner = ['-------------------------',f'Winner: {candidate[voteresult.index(max(voteresult))]}','-------------------------']
completelist = toplist + winner

for output in completelist:
    print(output)

output_file = os.path.join('/Users','ash.tao','Desktop','PyPoll','analysis','output.txt')
with open(output_file, "w") as datafile:
    for output in completelist:
        datafile.writelines(output)
        datafile.writelines("\n")
