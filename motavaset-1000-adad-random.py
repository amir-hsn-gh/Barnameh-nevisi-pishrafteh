import random

with open('data.txt', 'w') as f:
    for i in range(1000):
        num = random.randint(1, 100)
        f.write(f"{num}\n")

numbers = []
with open('data.txt', 'r') as f:
    for line in f:
        numbers.append(int(line))

print(f"tedade adad: {len(numbers)}")
print(f"majmoe adad: {sum(numbers)}")
print(f"miyangine adad: {sum(numbers)/len(numbers):.2f}")