# Programs of Stock Trasanction :
#number of shares purchases = 2 000 
#paiement per shares 40.00
#money paid in total = number of shares * pay_per_shares
# ammont paid to stock =( number of shares * pay_per_shares)*0.03
#Total_out = amount + amount paid to stock

#number of shares sold = 2000
#paiment per shares = 42.75
#amount_sold = 42.75 * 2000
#payement to stock = (42.75 * 2000)*0.03
#total_in = amount + amount paid to tod

STOCKBROKER = 3/100
numberOfStock = 2000
price_paid = 40.0 
total_out = numberOfStock*price_paid
print("the amont of money paid for the stock: ",total_out,"$",sep='')
print("the amount of commision paid to broker:",total_out*STOCKBROKER,"$",sep='')
total_out += total_out*STOCKBROKER
price_paid= 42.75 
total_in = numberOfStock*price_paid
print("the amount of money stock is sold:",total_in,"$",sep='')
print("the amount of commision paid to broker:",total_in*STOCKBROKER,"$",sep='')
total_in -= total_in*STOCKBROKER
print("money left:",total_in-total_out)