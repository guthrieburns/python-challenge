import os
import csv
from decimal import *

bank_csv = os.path.join("Resources", "budget_data_1.csv")

date = []
revenue = []

with open(bank_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        date.append(row[0])

        revenue.append(row[1])

    date.remove("Date")
    revenue.remove("Revenue")

    total_months = len(date) - 1
    
    total_revenue = sum(Decimal(i) for i in revenue)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + str(total_revenue))
    print("Average Revenue Change: ")
    print("Greatest Increase in Revenue: ")
    print("Greatest Decrease in Revenue: ")
    
    #print(str(sum_of_revenue))

#new_csv = zip(date, revenue)

#output_file = os.path.join("final_bank.csv")

#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    #writer.writerow(["Date", "Revenue"])

    #writer.writerows(new_csv)