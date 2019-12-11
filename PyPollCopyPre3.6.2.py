### Module 3.4.1 Python Dependencies, Modules and Packages

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

##################################

## Read Analyze and write the Election Results. 3.4.4
import os
import csv

# Assign variables for files
file_to_load = "election_results.csv"
file_to_save = "election_analysis.txt"

# Initialize variables
# total vote counter
total_votes = 0
# Candidate Name
candidate_options =[]
# dictionary with candidate names and their total votes
candidate_votes = {}
# Additional variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

##Open the election results. Read and analyze the data.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
## Now loop thru each row to get a data set of unique candidates their vote counts. Observe the headers observation
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1  # Add to the total vote count 
        candidate_name = row[2]  # Add pointer for candidate name retrieval for each row
        # Now, still processing rows. Add the candidate name to the candidate list if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)   # Track the candidate votes
            candidate_votes[candidate_name] = 0 # add a vote for that candidate
        candidate_votes[candidate_name] +=1 #add 1 vote to candidate running total.  
      
## Now open a file for writing. some loops, calculations and write them to file.

with open(file_to_save, "w") as txt_file:  # sets the file to open

    for candidate in candidate_votes:  # for each candidate in our dictionary
        votes = candidate_votes[candidate]   # Set the vote count per candidate
        vote_percentage = float(votes) /float(total_votes) * 100 # Calulate the percentage of votes
        #print(f"{candidate} received {vote_percentage:.2f}% of the vote") # Print Candidate name and percentage.

        if (votes > winning_count) and (vote_percentage > winning_percentage): # still for each candidate: if candidate votes  and % are greater than var\counter, set value of var\counter to this candidate.
            # If true then set winning_count = votes and winning_percent vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate   # And, set the winning_candidate equal to the candidate's name.
        ##print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") #print each candidates name, vote percentage and vote count

    ### Now create a print variable containing the winning summary  and print it
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n")
    #print(winning_candidate_summary)

# Print the final vote count to the terminal and to the text file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)