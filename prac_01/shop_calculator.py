items = int(input("Enter number of items: "))
total_price = 0

while items <= 0:
    print('Invalid Number of Items')
    items = int(input("Enter number of items: "))


for i in range(0, items):
    item_price = float(input("Enter price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    print("Total price for " + str(items) + " items is $" + "%.2f" % (total_price*0.9))
else:
    print("Total price for " + str(items) + " items is $" + "%.2f" % total_price)

