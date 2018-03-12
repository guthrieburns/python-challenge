import os
import csv
from decimal import *

poll_csv = os.path.join("Resources", "election_data_2.csv")

voter = []
county = []
candidate = []

#reading the csv and adding to lists
with open(poll_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        voter.append(row[0])

        county.append(row[1])

        candidate.append(row[2])

    #voter.remove("Voter ID")
    voter.pop(0)
    county.pop(0)
    candidate.pop(0)

    total_votes = len(voter)

    print("Election Results")
    print("---------------------")
    print("Total Votes:" + str(total_votes))
    print("---------------------")