sal = int(input("sale morede nazar ra vared konid:"))

def isLeapYear(year):
    yearCyrcle = [1, 5, 9, 13, 17, 22, 26, 30]
    remainder = year % 33
    return remainder in yearCyrcle

if isLeapYear(sal):
    print("Sale kabiseh ast.")
else:
    print("Sale kabiseh nist.")
