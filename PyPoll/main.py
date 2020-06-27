#importing
import os
import csv

#csv path
csvpath=os.path.join ("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    # defining the variables
    total_votes = 0
    candidates = []
    vote_khan=0
    vote_correy=0
    vote_li=0
    vote_otooley=0

    #for loop
    for row in csvreader:
        total_votes+=1
        if row[2] not in candidates:
            candidates.append(row[2])
            #print(canddiates) was done to get the list of candidates for the rest of the loop
        if row[2]=="Khan":
            vote_khan+=1
        if row[2]=="Correy":
            vote_correy+=1
        if row[2]=="Li":
            vote_li+=1
        if row[2]=="O'Tooley":
            vote_otooley+=1


  
   
    

#Percentage of vote
khan_percent=(vote_khan/3521001)*100
correy_percent=(vote_correy/3521001)*100
li_percent=(vote_li/3521001)*100
otooley_percent=(vote_otooley/3521001)*100

#determining winner
if khan_percent>50:
    winner="Khan"
if correy_percent>50:
    winner="Correy"
if li_percent>50:
    winner="Li"
if otooley_percent>50:
    winner="O'Tooley"
#printing to terminal
print ("Total votes: " + str(total_votes))
message =f"Khan: {khan_percent}%  ({vote_khan})"
message_2=f"Correy: {correy_percent}%  ({vote_correy})"
message_3=f"Li: {li_percent}%  ({vote_li})"
message_4=f"O'Tooley: {otooley_percent}%  ({vote_otooley})"
print(message)
print(message_2)
print(message_3)
print(message_4)
print ("Winner: " + str(winner))

#printing to txt file
print(message, file=open ("analysis.txt", "a"))
print(message_2, file=open ("analysis.txt", "a"))
print(message_3, file=open ("analysis.txt", "a"))
print(message_4, file=open ("analysis.txt", "a"))
print ("Winner: " + str(winner), file=open ("analysis.txt", "a"))
    