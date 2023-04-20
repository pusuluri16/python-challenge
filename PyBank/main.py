# CSV module to read and create files.
import csv

# Read and open the csv file. Using with will also close the file after finishing with it.
with open('PyBank/Resources/budget_data.csv') as file:
    #Read the file using csv reader function.
    file_reader = csv.reader(file, delimiter= ',')

    #Store header information into a varaiable.
    header = next(file_reader)

# List of profit and losses and  months.
    profit_loss =[]
    months =[]

# Define variables
    total_months = 0
    net_total_amount = 0
    monthly_changes = [] 
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month =''
    greatest_decrease_month = ''
    

    # Read each row of data after the header.
    for row in file_reader:
        months.append(row[0])
        profit_loss.append(row[1])

# Total number of months in the dataset.
total_months = len(months)

# Iterate through profit and loss list to find the net total amount.
for value in profit_loss:
    net_total_amount = net_total_amount+int(value)

# Iterate through profit and loss list to avaerage of charges.
for i in range(1,len(profit_loss)):
    monthly_changes.append(int(profit_loss[i])-int(profit_loss[i-1])) 
    

# Caluculating average change and rounding it to 2 decimal points.
average_change = round((sum(monthly_changes)/len(monthly_changes)),2)

# Caluculate greatest increase.
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(max(monthly_changes))+1]

# Caluculate greatest decrease.
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(min(monthly_changes))+1]

# Prinitng the analysis to the terminal.
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total_amount}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the analysis to the file.
output_file = open("PyBank/analysis/PyBank_Analysis.txt", "w")
output_file.write("Financial Analysis\n")
output_file.write("----------------------------\n")
output_file.write(f"Total Months: {total_months}\n")
output_file.write(f"Total: ${net_total_amount}\n")
output_file.write(f"Average Change: ${average_change}\n")
output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
output_file.close()