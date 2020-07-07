import os
import csv

# Get current working directory --> make sure to be on "Desktop/Bootcamp/HW/python-challenge/PyBank". if not, copy  
now = os.getcwd()

# String path together; again start from "Desktop/Bootcamp/HW/python-challenge/PyBank"
csvpath = os.path.join(now, 'Resources', 'budget_data.csv')
#print(csvpath)

# Variables & lists for calculations
month_count = 0 
profits = [] # daily profit/loss, then add them up
change = [] # daily profit/loss changes, the calculate average, max, min

# Open CSV file, count months and assign profits to list
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    
    next(reader)

    for row in reader:
        month_count += 1

        profits.append(int(row[1]))

# Add total profits
total = 0
for i in profits:
    total = total + i

# Calculate daily changes in profits
for i in range(len(profits)-1):  
    x = profits[i]
    
    y_index = i + 1 # index offset for profits in t+1
    y = profits[y_index] 
    
    daily_change = y - x # difference or daily change
    change.append(daily_change)
    row.append(daily_change)

average_change = float('%2.f'%(sum(change) / len(change)))

max_increase = max(change)
#for row in change:
    #if row[0] =="

max_decrease = min(change)

# Output table
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: (${max_increase})')
print(f'Greatest Decrease in Profits: (${max_decrease})')

"""with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    for row in reader:
        row_count += 1
        
        sum_profits.append(row[1]) 

print(row_count)
print(sum(sum_profits)) """


""" with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1]) """