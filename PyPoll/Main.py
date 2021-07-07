#import dependencies
import os 

import csv

# Name file path
filepath = "C:/Users/MW/Desktop/Homework/Python-Challenge/python-challenge/PyPoll/Resources/election_data.csv"

#Create dictionary
candidates = {}
#Open file, find header (supposed to pull off header, but I can't get past the StopIteration issue)
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1
        total = candidates.values()
        TVotes = sum(total)
        list_candidates = candidates.keys()
        VotesEach = [f'{(x/TVotes)*100:.3f}%' for x in candidates.values()]
        Winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        Winner
print("Election results")
print("--------------------------------")
print(f" Total votes: {int(TVotes)}")
print("---------------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote} , {VotesEach[i]}') 
    i+=1
print("------------------------------")
print(f" Winner: {Winner}")
print("------------------------------")

output_path = "C:/Users/MW/Desktop/Homework/Python-Challenge/python-challenge/PyPoll/Analysis/Analysis.txt"

with open(output_path, "w") as txt:

    txt.write("Election results\n")

    txt.write("--------------------------------------------------\n")

    txt.write(f" Total votes: {int(TVotes)}")

    txt.write(f"{candidate}, {vote} , {VotesEach[i]}") 
   

    txt.write(f" Winner: {Winner}")

   