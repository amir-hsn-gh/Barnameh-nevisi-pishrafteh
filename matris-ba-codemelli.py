import random
import hashlib

def generate_vectors(seed_value, num_vectors=10, vector_length=10):
    random.seed(seed_value)
    
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

def print_vectors(vectors, set_number):
    print(f"\nbordarhaye {set_number}:")
    for i, vector in enumerate(vectors, 1):
        print(f"bordar {i}: {''.join(map(str, vector))}")

def print_matrix(vectors, set_number):
    print(f"\nmatris 10 * 10 ({set_number}):")
    print("+" + "-"*21 + "+")
    for row in vectors:
        print("| " + " ".join(map(str, row)) + " |")
    print("+" + "-"*21 + "+")

def main():
    national_code = input("codemelli ra vared konid: ")
    
    if not national_code.isdigit() or len(national_code) != 10:
        print("codemelli bayad 10 raghami bashad")
        return
    
    seed1 = int(hashlib.sha256(national_code.encode()).hexdigest(), 16) % (10**8)
    seed2 = seed1 + 1
    
    vectors_set1 = generate_vectors(seed1)
    vectors_set2 = generate_vectors(seed2)
    
    print("\n" + "="*50)
    print_vectors(vectors_set1, 1)
    print_matrix(vectors_set1, 1)
    
    print("\n" + "="*50)
    print_vectors(vectors_set2, 2)
    print_matrix(vectors_set2, 2)

if __name__ == "__main__":
    main()