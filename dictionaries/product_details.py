# Generate Bill

answer = 'yes'
prod_dict = {}
prod_details = {}
bill = 0

# While Loop

while answer == 'yes':
    product = str(input('Enter Product Name: '))
    price = float(input('Enter Product Price: '))
    qty = int(input('Enter Quantity Purchased: '))

    # Creating dictionary of price, qty
    prod_details['price'] = price
    prod_details['quantity'] = qty

    # Creating nested list
    prod_dict = prod_details

    # Calculate Bill
    bill += price*qty

    answer = input('Add more products? (yes/no): ')
# print(prod_dict)

# Total Bill
print(f'Total bill = {bill}')
