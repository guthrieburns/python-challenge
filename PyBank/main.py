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

    total_months = len(date)
    total_revenue = sum(Decimal(i) for i in revenue)
    average_revenue = total_revenue/40

    revenue = list(map(int, revenue))

    max_revenue = max(revenue)
    min_revenue = min(revenue)

    max_index = revenue.index(max(revenue))
    max_date = date[max_index]
    
    min_index = revenue.index(min(revenue))
    min_date = date[min_index]

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(average_revenue))
    print("Greatest Increase in Revenue: ($" + str(max_revenue) + ") " + str(max_date))
    print("Greatest Decrease in Revenue: ($" + str(min_revenue) + ") " + str(min_date))
    
    

#new_csv = zip(date, revenue)

#output_file = os.path.join("final_bank.csv")

#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    #writer.writerow(["Date", "Revenue"])

    #writer.writerows(new_csv)