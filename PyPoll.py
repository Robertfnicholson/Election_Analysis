# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = 'C:/Users/RFNichol/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:/Users/RFNichol/analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Write some data to the file.
     txt_file.write("Hello World")

     # Close the file
     txt_file.close()
