import random
from functools import reduce

class Pipeline:
    def __init__(self, data):
        self.data = data
    
    def __or__(self, processor):
        return Pipeline(processor(self.data))

def generate_numbers(count=1000):
    for _ in range(count):
        yield random.randint(1, 100)

def save_to_file(numbers, filename='data.txt'):
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")
            yield num

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total, count

def run_pipeline():
    pipeline = Pipeline(generate_numbers())
    
    result = (pipeline
              | (lambda gen: save_to_file(gen))
              | calculate_average
             )
    
    total, count = result.data
    
    if count > 0:
        print(f"tedade adad: {count}")
        print(f"majmoe adad: {total}")
        print(f"miyangine adad: {total/count:.2f}")
    else:
        print("adadi vojod nadarad.")

if __name__ == "__main__":
    run_pipeline()
