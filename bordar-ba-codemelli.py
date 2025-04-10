import random
import hashlib

def generate_vectors(national_code, num_vectors=10, vector_length=10):
    seed = int(hashlib.sha256(national_code.encode()).hexdigest(), 16) % (10**8)
    random.seed(seed)
    
    vectors = []
    for _ in range(num_vectors):
        while True:
            vector = [random.randint(0, 9) for _ in range(vector_length)]
            
            valid = True
            for i in range(vector_length - 1):
                if vector[i] == vector[i+1]:
                    valid = False
                    break
            
            if valid:
                vectors.append(vector)
                break
    
    return vectors

def main():
    national_code = input("codemelli ra vared konid: ")
    
    if not national_code.isdigit() or len(national_code) != 10:
        print("bayad 10 raghami bashad!")
        return
    
    vectors = generate_vectors(national_code)
    
    print("\nbordarha:")
    for i, vector in enumerate(vectors, 1):
        print(f"bordar {i}: {''.join(map(str, vector))}")

if __name__ == "__main__":
    main()