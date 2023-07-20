import os
import csv
poll_data = os.path.join('/Users/theresakim/Documents/northwestern/module 03 python/Starter_Code/PyPoll/Resources/election_data.csv')

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

votes_charles = []
votes_diana = []
votes_raymon = []
total_votes = 0
percent_charles = 0
percent_diana = 0
percent_raymon = 0

with open(poll_data, 'r') as file:

    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        charles = row[0]
        diana = row[1]
        raymon = row[2]
        votes_charles.append(charles)
        votes_diana.append(diana)
        votes_raymon.append(raymon)

        if row[2] == "Charles Casper Stockham":
            votes_charles.append(row[0])
        elif row[2] == "Diana DeGette":
            votes_diana.append(row[1])
        elif row[2] == "Raymon Anthony Doane":
            votes_raymon.append(row[2])

total_votes = len(row[0]) + len(row[1]) + len(row[2])
total_votes_charles = len(row[0])
total_votes_diana = len(row[1])
total_votes_raymon = len(row[2])
percent_charles = 100 * (total_votes_charles / total_votes)
percent_diana = 100 * (total_votes_diana / total_votes)
percent_raymon = 100 * (total_votes_raymon / total_votes)

print("")
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"Charles Casper Stockham: {percent_charles:.3f}% ({total_votes_charles})")
print(f"Diana DeGette: {percent_diana:.3f}% ({total_votes_diana})")
#print(f"Raymon Anthony Doane: " {percent_raymon:.3f}% ({total_votes_raymon}))
print("----------------------")
#print(f"Winner: {winner}")
#print("----------------------")

# out = open("pypoll_solved.txt", "w")

# out.write("Election Results")
# out.write("----------------------")

# out.close()