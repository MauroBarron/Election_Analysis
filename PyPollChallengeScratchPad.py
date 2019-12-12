### Py Poll Challenge Scratchpad

#1. Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
#2. Create a list for the counties.
#3. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
#4. Create an empty string that will hold the county name that had the largest turnout.
#5. Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
#6. Inside the with open() function where you are outputting the file, do the following: 
#• Create three if statements to print out the voter turnout results similar to the results shown above.
#• Add the results to the output file.
#Print the results to the command line.

### Prep environment
import csv
dir(csv)

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

#Challenge - Create a list for counties and a dictionary where county is key and votes casts are the values.




##Open the election results. Read and analyze the data.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    

    print(election_data)
# #election_data.close

###  Practice pulling
# first get the environment ready to travel with OS commands
# and get it ready to work with CSV.
# import csv
# import os
# #assign variable for path and join file to load
# file_to_load = os.path.join("Resources","election_results.csv")
# # now open the file and read it.
# with open(file_to_load) as election_data:
#     print(election_data)

 #######################
 
# Write to Files with Python 3.4.3
# import os
# file_to_save = os.path.join("Analysis","election_analysis.txt")
# # Use the open() functionwith the "w" to write
# outfile = open(file_to_save, 'w')
# # write some data to the file
# outfile.write("Hello World")
# # close the file
# outfile.close

## now do it with the With statement
# import os
# file_to_save = os.path.join("Analysis","election_analysis.txt")
# # now use the With statement
# with open(file_to_save, 'w') as txt_file:
#     #now write some text
#     #txt_file.write("Arapahoe, Denver, Jefferson")
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")


### code below commented out. 


    ##################################
    ## Read the Election Results. 3.4.4
    import os
    import csv

    # Assign a variable to load file
    #file_to_load = "election_results.csv"
    #file_to_load = os.path.join("election_analysis","election_results.csv")
    #  Assign a variable to save the file to..
    #file_to_save = os.path.join("analysis/Election_Analysis/election_analysis.txt")
    #with open(file_to_load) as election_data:
        #To do: read and analyze the data
    #   file_reader = csv.reader(election_data)
        #for row in file_reader:
            #print(row)
            #print(row[0])    
    # headers = next(file_reader)
    #  print(headers) 
        
        
    ### 3.5.1 Get the Total Votes
    #Open the election results and read file
        #Use ctrl + c to interrupt code run


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
    #Open the election results
    # Add needed variables

    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0



    with open(file_to_load) as election_data:
        #To do: read and analyze the data
        file_reader = csv.reader(election_data)
        
    # Read the data.
        headers = next(file_reader)
        #print each row in file_reader
        for row in file_reader:
            #  Add to the total vote count 
            total_votes += 1 
            # print candidate name for each row
            candidate_name = row[2] 
            #Add the candidate name to the candidate list if not already there
            if candidate_name not in candidate_options:
                # Add the candidate name to the candidates list
                candidate_options.append(candidate_name)
                # Track the candidate votes
                candidate_votes[candidate_name] = 0
                # add a vote for that candidate
            candidate_votes[candidate_name] +=1
        
    #  Print the total votes.
        #print(total_votes)

    #  Print the Candidate list.
    #print(candidate_options)

    #  Print the Candidate votes dictionary.
    #print(candidate_votes)
    
    ### Determine percentage of votes

    # iterate thru the candidate dictionary
    #for candidate in candidate_votes:
        # Get the vote count per candidate
        # votes = candidate_votes[candidate]
        # Calulate the percentage of votes
        #   vote_percentage = int(votes) /int(total_votes) * 100
        # Print Candidate name and percentage.
    #     print(f"{candidate} received {vote_percentage:.2f}% of the vote")

    ### Now determine the winning candidate.


    ### Save results to text file

    # with open(file_to_save, "w") as txt_file:

    # # Print the final vote count to the terminal.
    #     election_results = (
    #         f"\nElection Results\n"
    #         f"-------------------------\n"
    #         f"Total Votes: {total_votes:,}\n"
    #         f"-------------------------\n")
    #     print(election_results, end="")
    #     # Save the final vote count to the text file.
    #     txt_file.write(election_results)

    ## Loop thru data
    # iterate thru the candidate dictionary
    with open(file_to_save, "w") as txt_file:



        for candidate in candidate_votes:
            # Get the vote count per candidate
            votes = candidate_votes[candidate]
            # Calulate the percentage of votes
            vote_percentage = float(votes) /float(total_votes) * 100
            # Print Candidate name and percentage.
            #print(f"{candidate} received {vote_percentage:.2f}% of the vote")

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate
            ##print(f"{candidate:} {vote_percentage:.1f}% ({votes:,})\n")
            ##print(f"{winning_candidate} received {winning_count} votes, representing {winning_percentage:.2f}% of the vote."
            #   #print f" {winning_candidate} is the winner of the election!!")
            ##print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        ### Now print the winning summary
        winning_candidate_summary = (
            f"-------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n")
        #print(winning_candidate_summary)

    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)