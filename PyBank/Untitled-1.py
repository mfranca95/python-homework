# %%
from pathlib import Path
import csv

## Initializing variables

menu_list = []
sales_list = []
product_report = {
    "01-count": 0,
    "02-revenue": 0,
    "03-cogs": 0,
    "04-profit": 0,
}
report = {}


## Logic for data reading

with open('python-homework/PyRamen/Resources/menu_data.csv', 'r') as menu_csv:
    menu = csv.reader(menu_csv)
    next(menu)
    for item in menu:
        menu_list.append(item)

with open('python-homework/PyRamen/Resources/sales_data.csv', 'r') as sales_csv:
    sales = csv.reader(sales_csv)
    next(sales)
    x = 0
    for money in sales:
        sales_list.append(money)
        sales_list[x][3] = int(sales_list[x][3])



## Logic for Data manipulation

for looper in menu_list:
    report[looper[0]] = {"01-count": 0,"02-revenue": 0,"03-cogs": 0,"04-profit": 0}
    x = 0
    y = 0
    for inner in sales_list:
        if looper[0] == inner[4]:
            inner[3] = int(inner[3])
            x = inner[3]
            report[looper[0]]['01-count'] += x
    y = y + 1
print (report)




