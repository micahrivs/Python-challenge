#importing the path and csv
import os
import csv

#making the file path and taking the csv file from Resources
filepath = os.path.join('.', 'Resources', 'election_data.csv')


#reading  csv and identifying which delimeter was used to seperate the words
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #reading the header
    csv_header = next(csvreader)
    candidate_list = [candidate[2] for candidate in csvreader]
    
#getting the total votes
total_votes = len(candidate_list)

#making a candidate list based on the votes
canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

#sorting list to find the winner
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

#printing results
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")


#for loop for candidates winner
for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("----------------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("----------------------------------")

# making a text file to save it on the analysis folder
# printing elction results
filepath = os.path.join('.', 'analysis', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("----------------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("----------------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("----------------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("----------------------------------", file=text_file)

