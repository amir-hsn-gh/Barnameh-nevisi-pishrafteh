income = int(input("adad ra vared konid:"))

if income < 0:      rate = 0.00
if income < 8925:   rate = 0.10
if income < 36250:  rate = 0.15
if income < 87850:  rate = 0.23
if income < 183250: rate = 0.28
if income < 398350: rate = 0.33
if income < 400000: rate = 0.35
else:               rate = 0.396

print("rate: ", rate)