### Module 3.4.1 Python Dependencies, Modules and Packages

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

### Import the datetime dependency.
# Import datetime dependency
#import datetime
# use the now () attribute  on the datetime dependency
#now = datetime.datetime.now()

# print the present time.
#print("the time right now is,", now)

### Import CSV Module
#import csv
#dir(csv)

###################################

### Reading data from a file.

##  Direct Path Method
# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
#election_data = open(file_to_load, 'r')
#close the file
#election_data.close

# ### use the With statement
# # Assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'

# with open(file_to_load) as election_data:
# # Open the election results and read the file
#     # do something. read the file for analysis.
#    print(election_data)
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

##################################
## Read the Election Results. 3.4.4
import os
import csv
# Assign a variable to load file
file_to_load = os.path.join("Resources/election_results.csv")
#  Assign a variable to save the file to..
file_to_save = os.path.join("analysis/election_analysis.txt")

#Open the election results and read file
    #Use ctrl + c to interrupt code run
with open(file_to_load) as election_data:
    #To do: read and analyze the data
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row)
        #print(row[0])    
    headers = next(file_reader)
    print(headers)    
#Commmit your code  3.4.5 



