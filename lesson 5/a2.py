actual_cost = float(input("Enter the actual price: "))
selling_cost = float(input("Enter the selling price: "))

if (selling_cost > actual_cost):
    cost = selling_cost - actual_cost
    print("Total Profit = {0}",format(cost))
else:
    print("No profit")