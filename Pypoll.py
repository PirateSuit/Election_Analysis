# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#Read data from a file (3.4.2)

# Done with direct path:

#Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# #Open the election results and read the file.
# with open(file_to_load) as election_data:

# # To do: perform analysis.
#     print(election_data)
# # Close the file.
# election_data.close()

# Done with indirect path:

# import csv
# import os

# #Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# #Open the election results and read the file.
# with open(file_to_load) as election_data:

#     #Print the file object:
#     print(election_data)

# # WRITING FILES TO PYTHON (3.4.3):

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # ADDING DATA TO THE CREATED TEXT FILE:

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
# # Write some data to the file.
#     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# THE "\n" PUTS THINGS ONTO A NEW LINE.


# # Close the file
# txt_file.close()

# READ THE ELECTION RESULTS...AND THEN ANALYZE AND ORGANIZE AND PRINT THEM. (3.4.4 - 3.5.5)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options.
candidate_options = []

# Declare an empty dictionary for votes.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to a text file.
with open(file_to_save, "w") as txt_file:
                
    # After opening the file, print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Create a variable and print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        print(candidate_results)

        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = vote and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # To do: print out the winning candidate, vote count, and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

 

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)







        



