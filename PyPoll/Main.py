import os
import csv

csvpath = r"/Users/williammdavis/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

num_votes = 0
#candidate_list = []
#candidate_votes = {}

#votes = {}
Otooley_votes = 0
Correy_votes = 0
Khan_votes = 0
Li_votes = 0

#winner_candidate = ""
#winner_num = {}

output_file = r"/Users/williammdavis/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_results.txt"

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # read csv and skip header
    csv_header = next(csvreader)
    print(csv_header)
    for row in csvreader:
        num_votes = num_votes + 1
        # print(num_votes)
        candidate_name = row[2]
        if (row[2]) == "Khan":
            Khan_votes += 1
        elif (row[2]) == "O'Tooley":
            Otooley_votes += 1
        elif (row[2]) == "Correy":
            Correy_votes += 1
        else:
            Li_votes += 1
    #test: print(Khan_votes)

    # percentage votes = candidate vote/total vote *100
    K_percentage_vote = float(Khan_votes) / float(num_votes) * 100
    O_percentage_vote = float(Otooley_votes) / float(num_votes) * 100
    C_percentage_vote = float(Correy_votes) / float(num_votes) * 100
    L_percentage_vote = float(Li_votes) / float(num_votes) * 100

    #test: print(L_percentage_vote)

    winner_candidate = max(Khan_votes, Otooley_votes, Correy_votes, Li_votes)

if winner_candidate == Khan_votes:
        winner_candidate = "Khan"
elif winner_candidate == Otooley_votes:
        winner_candidate = "O'Tooley"
elif winner_candidate == Correy_votes:
        winner_candidate = "Correy"
else:
        winner_candidate = "Li"
#print(winner_candidate)

# print("Election Results")
# print("------------------------")
# print("Total Votes:" + str(num_votes))
# print("------------------------")
# print("Khan: " + str(Khan_votes)+ "   "  + str(K_percentage_vote)+ "%")
# print("Li: " + str(Li_votes)+ "   "  + str(L_percentage_vote)+ "%")
# print("O'Tooley: " + str(Otooley_votes)+ "   " + str(O_percentage_vote)+"%" )
# print("Correy:" + str(Correy_votes) + "   " + str(C_percentage_vote) + "%")
# print("------------------------")
# print("winnner: " +(winner_candidate))

#write data to csv file


results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {num_votes}\n"
    f"-------------------------\n"
    f"O'Tooley: {Otooley_votes} {O_percentage_vote:.2f}%\n"
    f"Correy: {Correy_votes} {C_percentage_vote:.2f}%\n"
    f"Li: {Li_votes} {L_percentage_vote:.2f}%\n"
    f"Khan: {Khan_votes} {K_percentage_vote:.2f}%\n"
    f"Winner: {winner_candidate}"
)
print(results)
with open(output_file, "w") as txt_file:
    txt_file.write("results")



