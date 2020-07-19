import os
import csv

csvpath = r"/Users/williammdavis/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"
num_votes= 0
candidate_list = []
candidate_votes={}
votes ={}

winner_candidate=""
winner_num={}



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
            num_votes +=1
            candidate_name= row[2]
            if candidate_name not in candidate_list:
                    #add names to list
                    candidate_list.append(candidate_name)
                    #set the dictionary
                    candidate_votes[candidate_name]=0
                    #add votes to candidate
                    candidate_votes[candidate_name]=candidate_votes[candidate_name]+1
                    print(candidate_votes)
    
    for candidate in candidate_votes:
            print([candidate])
            votes=candidate_votes(candidate)
            votes_percentage = float(votes) / float(num_votes) * 100
            print(votes_percentage)
            if (votes>winner_num):
                    winner_num = votes
                    winner_candidate = candidate
                    print(str(winner_candidate))

                        

            
#print results
print("Election Results")
print("------------------------") 
        print(f"Total Votes: " + str(num_votes))
print("------------------------") 
        print(f"{candidate}: {votes_percentage}% {votes}")
        #print(f"Winner: {winner_candidate})
           
            
        
