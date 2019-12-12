### Module 3.4.1 Python Dependencies, Modules and Packages

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

##################################

## Read Analyze and write the Election Results. 
import os
import csv

# Assign variables for files
file_to_load = "election_results.csv"
file_to_save = "election_analysis.txt"

# Create and Initialize variables
# total vote counter
total_votes = 0
candidate_options =[]  # List of Candidate Names with confusing name.
candidate_votes = {}  # dictionary with candidate names and their total votes
# Additional variables for processing winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Challenge  variables - Create a list for counties and a dictionary where county is key and votes casts are the values.
county = [] # List of County names.
county_votes ={} # Dictionary for counties containing name can votes casts.
county_winner = "" #empty string for county winner
cwinning_count = 0 #counter for determing winning count
cwinning_percentage = 0 # counter for determing winning percentage

##Open the election results. Read and analyze the data.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
## Now loop thru each row to process candidate and county vote data.
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1  # Add to the total vote count 
        ## nowprocess candidate and county data for each row
        #county_name = row[1]  # declare county name set second column as the location for county_name
        candidate_name = row[2]  # Add pointer for candidate name retrieval for each row
        # Add the candidate name to the candidate list if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)   # Add candidate to candidate list
            candidate_votes[candidate_name] = 0 # initialize candidate votes at zero
        candidate_votes[candidate_name] +=1 #add 1 vote to candidate running total.   
        
        ## Challenge:  Process county voting data.
        county_name = row[1]  # declare county name set second column as the location for county_name
        # # Now add the county name to list and update dictionary.
        if county_name not in county: #check presence of current county in county list
            county.append(county_name) # add county to county list
            county_votes[county_name] = 0 # set vote count for couty to zero
        county_votes[county_name] +=1 # add a vote for that county
         
## Now open a file for writing. Do some loops, calculations and write them to file.

with open(file_to_save, "w") as txt_file:  # sets the file to open for write
    # Print the final vote count to the terminal and to the text file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print County Header.
    county_header = (
        f"\nCounty Votes:\n")
    print(county_header, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_header)

    #Calculate county vote data.
    for county in county_votes:  # for each county in our dictionary
        cvotes = county_votes[county]   # Set the vote count per candidate
        cvote_percentage = float(cvotes) /float(total_votes) * 100 # Calulate the percentage of votes
        
    # Determine the winning county.
        if (cvotes > cwinning_count) and (cvote_percentage > cwinning_percentage): # if # If true then set winning_count = votes and winning_percent vote_percentage.# And, set the winning_candidate equal to the candidate's name.
            cwinning_count = cvotes
            cwinning_percentage = cvote_percentage
            county_winner = county 
        
        ## Now print County summary  to terminal and text file
        county_results = (f"{county}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results) # print county summary to terminal and file.
        txt_file.write(county_results)

    # Print the County Winner info to the terminal and to the text file.
    county_results = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_winner}\n"
        f"-------------------------\n")
    print(county_results)
    txt_file.write(county_results)

### Candidate Assessment
    # Calculate Candidate Vote data.
    for candidate in candidate_votes:  # for each candidate in our dictionary
        votes = candidate_votes[candidate]   # Set the vote count per candidate
        vote_percentage = float(votes) /float(total_votes) * 100 # Calulate the percentage of votes
        #print(f"{candidate} received {vote_percentage:.2f}% of the vote") # Print Candidate name and percentage.

    # Calculate candidate_vote and asses if it is the winning vote.
        if (votes > winning_count) and (vote_percentage > winning_percentage): # if # If true then set winning_count = votes and winning_percent vote_percentage.# And, set the winning_candidate equal to the candidate's name.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate   
        
        ## Now print Candidate summary  to terminal and text file
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") #sets a print variable for each candidates name, vote percentage and vote count
        print(candidate_results) # print each candidates results to terminal
        txt_file.write(candidate_results)

    ### Now create a print variable containing the winning summary  and print it
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------")

    #print winners name and save to text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    ## Now go have a drink!  Code is running successfully. Wow!!
    

