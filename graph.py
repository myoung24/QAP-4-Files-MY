# Display sales by month on a graph
# Author: Matt Young
# Date Created: 2023-Mar-22

import matplotlib.pyplot as plt

x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = []

for i in x_axis:
    while True:
        try:
            sales = float(input(f"Enter the total sales for {i}: "))
            y_axis.append(sales)
            break
        except:
            print("Must be a number. Try again")

plt.title("Total Sales by Month")
plt.plot(x_axis, y_axis, color='green', marker='o')
plt.xlabel("Month")
plt.ylabel("Sales ($)")

plt.grid(True)

plt.show()

exit()
