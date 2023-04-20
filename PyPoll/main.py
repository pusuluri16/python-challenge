# CSV module to read and create files.
import csv

# Read and open the csv file. Using with will also close the file after finishing with it.
with open('PyPoll/Resources/election_data.csv') as file:
    #Read the file using csv reader function.
    file_reader = csv.reader(file, delimiter= ',')

    #Store header information into a varaiable.
    header = next(file_reader)
# list of  "Voter ID", "County", and "Candidate".
    voters = []
    counties = []
    candidates = []
    all_rows = []
    votes_list = []
    winner_candidate = ''
    
# Read each row of data after the header.
    for row in file_reader:
        all_rows.append(row)
        voters.append(row[0])
        if(row[1] not in counties ):
            counties.append(row[1])
        if(row[2] not in candidates ):
            candidates.append(row[2])

#Define variables
total_votes = 0
total_candidates = 0

# Print to terminal and write to the file.
print("Election Results\n")
print("-------------------------\n")

output_file = open("PyPoll/analysis/PyPoll_Analysis.txt", "w")
output_file.write("Election Results\n")
output_file.write("-------------------------\n")

# The total number of votes/ 
total_votes =len(voters)
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
output_file.write(f"Total Votes: {total_votes}\n")
output_file.write("-------------------------\n")

# Iterate through each candiate.  
for candidate in candidates:
    # Initaite varaibles.
    votes_per_candidate = 0
    votes_percent_per_candidate = 0
    # Iterate through the list and caluculate votes per candiadte and percentage of votes.
    for row in all_rows:
        #Check if the row has the candiadte details 
        if(row[2] == candidate):
            #Increment the vote count if the condition is met.
            votes_per_candidate = votes_per_candidate+1
    #Caluculate votes percenatge and round it to 3 decimal points.
    votes_percent_per_candidate = round(((votes_per_candidate/total_votes)*100),3)

    # Print to terminal and write to the file
    print(f"{candidate}: {votes_percent_per_candidate}% ({votes_per_candidate})\n")
    output_file.write(f"{candidate}: {votes_percent_per_candidate}% ({votes_per_candidate})\n")

    votes_list.append(votes_percent_per_candidate)
    # Find the winner based on maximum votes polled.
    if(max(votes_list)==votes_percent_per_candidate):
        winner_candidate = candidate

# Print to terminal and write to the file
print("-------------------------\n")
print(f"Winner: {winner_candidate}\n")
print("-------------------------")
output_file.write("-------------------------\n")
output_file.write(f"Winner: {winner_candidate}\n")
output_file.write("-------------------------")

# Finally close the file after writing to it.
output_file.close()