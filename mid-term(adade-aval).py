def adade_aval(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def k_omin_adade_avale_bad_az_n(k, n):
    count = 0
    current = n + 1

    while True:
        if adade_aval(current):
            count += 1
            if count == k:
                return current
        current += 1

n = int(input("adade n ra vared konid: "))
k = int(input("adade k ra vared konid: "))
k_omin = k_omin_adade_avale_bad_az_n(k, n)

print(f"{k} omin adade avale bad az {n}: {k_omin}")