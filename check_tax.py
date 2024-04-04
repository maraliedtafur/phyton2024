price = input('how much did you pay?  ')

prince = float(price)
if prince >= 1.00:
    tax = 0.07
    print('Tax rate is: ' + str(tax))
else:  
    tax = 0
    print('Tax rate is: ' + str(tax))  