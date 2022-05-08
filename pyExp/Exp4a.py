import pricing
net_price = pricing.get_net_price(100,10.0,20)
print('Net price is: ',net_price)
net_tax = pricing.get_tax(100,10.0)
print('Tax is: ',net_tax)
