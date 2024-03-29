import csv

import os

#set path to csv file

file = os.path.join('election_data.csv')

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read the csv and convert into a list of dictionaries
with open(file) as election_data:
    reader = csv.DictReader(election_data)

    # For each row...
    for row in reader:
        print(". ", end="")

        # add to the total vote count
        total_votes = total_votes + 1

        # get the candidate name from each row
        candidate_name = row["Candidate"]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # and start tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print the results and export the data to our text file
with open(file, "w") as txt_file:

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage to terminal
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)


    # Print the final vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Print the winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)