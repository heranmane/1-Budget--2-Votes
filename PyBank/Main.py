import os
import csv

csvpath = r"/Users/williammdavis/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
profit_loss= 0
net_changes=[]
greatest_increасеse=["", 0]
greates_decrease=["", 9999999999]

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    date= []
    first_row= next(csvreader)
    profit_loss += int(first_row[1])
    previous_net=int(first_row[1])

    for row in csvreader:
        date.append(row[0])
        profit_loss += int(row[1])
        net_change=int(row[1])-previous_net
        net_changes+= [net_change]
        if net_change > greatest_increасеse[1]:
            greatest_increасеse[0]=row[0]
            greatest_increасеse[1]=net_change
        if net_change < greates_decrease[1]:
            greates_decrease[0]=row[0]
            greates_decrease[1]=net_change

#average net change 
average_change=sum(net_changes)/len(net_changes)

print("Financial Analysis")
print("------------------------")
print("Total Months: " +str(len(date)))
print("Total profit: " + str(profit_loss))
print("Average changes:" + str(average_change))
print("Greatest Increase:" + str(greatest_increасеse))
print("Greatest Decrease:" + str(greates_decrease))