import random

adade_random = [random.randint(1, 15) for _ in range(20)]
print("20 adade random: ", adade_random)

adade_random.sort(reverse=True)

def majmoe_adad(numbers, min_sum, max_sum):
    current_sum = 0
    selected_numbers = []
    
    for num in numbers:
        if current_sum + num > max_sum:
            continue
        current_sum += num
        selected_numbers.append(num)
        
        if min_sum <= current_sum <= max_sum:
            break

    if min_sum <= current_sum <= max_sum:
        return selected_numbers
    else:
        return None

result = majmoe_adad(adade_random, 50, 52)

if result:
    print(f"majmoe adad ba majmo beyne 50 ta 52: {result}")
    print(f"majmo: {sum(result)}")
else:
    print("hich majmoe adad ba majmo beyne 50 ta 52 mojod nemibashad.")