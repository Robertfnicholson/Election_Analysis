# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote
# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('/Users/RFNichol', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('/Users/RFNichol/analysis', 'election_analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
