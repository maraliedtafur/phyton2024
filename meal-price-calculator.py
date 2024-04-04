child_meal = float(input("What is the price of a child's meal?"))  
adult_meal = float(input("What is the price of an adult's meal?"))
num_childrens = int(input("How many children are there?"))
num_adults = int(input("How many adults are there?"))

subtotal = (num_childrens * child_meal) + (num_adults * adult_meal)

print(f"Subtotal: ${subtotal:.2f}")

tax_sales = float(input("What is the sales tax rate?"))

tax_rate = (subtotal * tax_sales) / 100

print(f"Sales Tax : ${tax_rate:.2f}")

total = subtotal + tax_rate

print(f"Total: ${total:.2f}")

payment_amount = float(input("What is the payment amount?"))

change = payment_amount - total

print(f"change: ${change:.2f}")

