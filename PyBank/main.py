#importing
import os
import csv

#csv path
csvpath=os.path.join ("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #declare variables
    months = []
    profit_loss=0
    greatest_profit = []
    greatest_loss= 0
    total_profit = 0
    change = []
    profit = []
    for r in csvreader:
        month = r[0]
        if month not in months:
            months.append(month)
        profit_loss += int(r[1]) # profit_loss = profit_loss + int(x[1])
        profit.append(r[1])
    #change in profit
    for i in range(len(profit)-1):
        changes = int(profit[i+1]) - int(profit[i])
        if changes not in change:
            change.append(changes)
    greatest = max(change)    
    greatest_loss = min(change)
    #months
    for a in range(len(change)):
        if max(change)==change[a]:
            gain_month=change[a]
           
            
        if min(change)==change[a]:
            loss_month=change[a]
#average profit loss
difference= (int(profit[85])) - (int(profit[0]))
average_pl= difference/(len(months)-1)

#print to terminal 
print('Total months = ' + str(len(months)))
print('Total P & L = ' + str(profit_loss))
print('Average Profit Loss = ' + str(average_pl))
print('Maximum Profit = ' + str(greatest) +' in ' + str(gain_month))
print('Greatest Loss = ' + str(greatest) + 'in ' + str(months[a+1]))
#print to txt file from https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3/36571602
print('Total months = ' + str(len(months)), file=open ("analysis.txt", "a"))
print('Total P & L = ' + str(profit_loss), file=open ("analysis.txt", "a"))
print('Average Profit Loss = ' + str(average_pl), file=open ("analysis.txt", "a"))
print('Maximum Profit = ' + str(greatest) +' in ' + str(gain_month), file=open ("analysis.txt", "a"))
print('Greatest Loss = ' + str(greatest) + ' in ' + str(months[a+1]), file=open ("analysis.txt", "a"))

   
            
            