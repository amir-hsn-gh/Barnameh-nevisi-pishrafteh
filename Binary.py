def decimal_to_binary(number):
    if number < 0:
        return "adade manfi vared shodeh. lotfan adade sahihe mosbat vared konid."
    return bin(number)[2:]

try:
    number = int(input("adade sahih ra vared konid: "))
    binary_representation = decimal_to_binary(number)
    print(f"namayesh binary adade {number}: {binary_representation}")
except ValueError:
    print("lotfan adade sahihe motabar vared konid.")