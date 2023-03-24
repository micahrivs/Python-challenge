# # import csv



# # file = open('Resources/budget_data.csv')
# # type(file)
# # csvreader=csv.reader(file)
# # header=[]
# # header=next(csvreader)
# # header

# # rows = []
# # for row in csvreader:
# #     rows.append(row)
# # rows

# #Importing the necessary modules/libraries
# import os
# import csv

# #Creating an object out of the CSV file
# budget_data = os.path.join("budget_data.csv")

# total_months = 0
# total_pl = 0
# value = 0
# change = 0
# dates = []
# profits = []

# #Opening and reading the CSV file
# with open(budget_data, newline = " ") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")

#     #Reading the header row
#     csv_header = next(csvreader)

#     #Reading the first row (so that we track the changes properly)
#     first_row = next(csvreader)
#     total_months += 1
#     total_pl += int(first_row[1])
#     value = int(first_row[1])
    
#     #Going through each row of data after the header & first row 
#     for row in csvreader:
#         # Keeping track of the dates
#         dates.append(row[0])
        
#         # Calculate the change, then add it to list of changes
#         change = int(row[1])-value
#         profits.append(change)
#         value = int(row[1])
        
#         #Total number of months
#         total_months += 1

#         #Total net amount of "Profit/Losses over entire period"
#         total_pl = total_pl + int(row[1])

#     #Greatest increase in profits
#     greatest_increase = max(profits)
#     greatest_index = profits.index(greatest_increase)
#     greatest_date = dates[greatest_index]

#     #Greatest decrease (lowest increase) in profits 
#     greatest_decrease = min(profits)
#     worst_index = profits.index(greatest_decrease)
#     worst_date = dates[worst_index]

#     #Average change in "Profit/Losses between months over entire period"
#     avg_change = sum(profits)/len(profits)
    

# #Displaying information
# print("Financial Analysis")
# print("---------------------")
# print(f"Total Months: {str(total_months)}")
# print(f"Total: ${str(total_pl)}")
# print(f"Average Change: ${str(round(avg_change,2))}")
# print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
# print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# #Exporing to .txt file
# output = open("output.txt", "w")

# line1 = "Financial Analysis"
# line2 = "---------------------"
# line3 = str(f"Total Months: {str(total_months)}")
# line4 = str(f"Total: ${str(total_pl)}")
# line5 = str(f"Average Change: ${str(round(avg_change,2))}")
# line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
# line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
# output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))


import os
#  Reading the CSV file
import csv
# Set path for file
filepath = os.path.join('.', 'Resources', 'budget_data.csv')

# Creating list to store data 
budget_data = []

# Opening the CSV
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    # Looping through the data to store in a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

# Calculating the total months
total_months = len(budget_data)

# Looping through the dictionary in order to calculate changes between months
previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    prev_amount = budget_data[i]["amount"]

# Calculating the total amount
total_amount = sum(row['amount'] for row in budget_data) 

# Calculating the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months-1), 2)

# Getting the  Greatest Increase and Decrease from the changes
get_increase = max(budget_data, key=lambda x:x['change'])
get_decrease = min(budget_data, key=lambda x:x['change'])


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')

filepath = os.path.join('.', 'analysis', 'PyBank_Results.txt')
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)