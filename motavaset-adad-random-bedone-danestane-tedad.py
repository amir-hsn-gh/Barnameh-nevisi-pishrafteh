import random

with open('data.txt', 'w') as f:
    for _ in range(1000):
        num = random.randint(1, 100)
        f.write(f"{num}\n")

total = 0
count = 0

with open('data.txt', 'r') as f:
    for line in f:
        if line.strip():
            num = int(line)
            total += num
            count += 1

if count > 0:
    average = total / count
    print(f"tedade adad: {count}")
    print(f"majmoe adad: {total}")
    print(f"miyangine adad: {average:.2f}")
else:
    print("adadi vojod nadarad.")