import os
import csv


# Get current working directory --> make sure to be on "Desktop/Bootcamp/HW/python-challenge/PyBank". if not, copy  
now = os.getcwd()
#print(now)

csvpath = os.path.join(now, 'Resources', 'election_data.csv')
#print(csvpath)

total_votes = 0
votes = []
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for row in csvreader:
        total_votes += 1
        
        vote = row[2]
        votes.append(vote)

        if vote not in candidates:
            candidates.append(vote)

""" print(candidates) """

# Count votes for each candidate
vote_count = [0 for candidate in enumerate(candidates)]
""" print(vote_count) """

# For loop to count votes and add to each candidate
for name in votes:
    index = candidates.index(name)
    vote_count[index] += 1

# Calculate vote percent for each candidate
vote_percent = []
for votes in vote_count:
    decimal = votes / total_votes
    percent = "{:.3%}".format(decimal)
    vote_percent.append(percent)

# Calculate winner
winner = max(vote_count)
winner_index = vote_count.index(winner)

# Print results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------""")
for i, candidate in enumerate(candidates):
    print(f'{candidate}: {vote_percent[i]} ({vote_count[i]})')
print("----------------------------""")
print(f"Winner: {candidates[winner_index]}")
print("----------------------------""")