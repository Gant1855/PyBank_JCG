import csv

import os
rows = []
#set path to csv file
file = os.path.join ('PyBank', 'Resources', 'budget_data.csv')
# name the variable header
header = []
total_months = 0
total = 0
average_change = 0
monthly_change = 0
previous_value = 0
total_monthlychange = 0
greatest_increase_profit = ["", 0]
greatest_decrease_profit = ["", 0]


# open the file in "read" mode ('r') and store the contents in the variable "text"
with open (file,'r') as text:
    readercsv = csv.reader(text, delimiter=",")
    
    # print the contents of the text file
   
    header = next(readercsv)
    for n, row in enumerate(readercsv):

        rows.append(row)
        # skip the month of Jan, but use the month of Feb
        if n > 0:
            monthly_change = (int(row[1]) - previous_value)
            total_monthlychange += monthly_change

            if greatest_increase_profit[1] > monthly_change:
                greatest_increase_profit[1] = monthly_change
                greatest_increase_profit[0] = row[0]
          

            if greatest_decrease_profit[1] > monthly_change:
                greatest_decrease_profit[1] = monthly_change
                greatest_decrease_profit[0] = row[0]


        total += int(row[1])
        previous_value = int(row[1])


average_change = ((total_monthlychange)/(len(rows)-1))



print(row)
total += int(row[1])
monthly_change = -1*(int(row[1]) - previous_value)
print(monthly_change)
previous_value = int(row[1])


print("Financial Analysis")
print("-------------------------------------")

print("The Total Months:", len(rows))
print("Total: $",total)
print("Average_Change: $ ", average_change) 
print("Greastest_Increase_Profit: $ ", greatest_increase_profit[0],greatest_increase_profit[1])
print("Greatest_Decrease: $ ", greatest_decrease_profit[0],greatest_decrease_profit[1])
