import random
import hashlib

def generate_vectors(seed_value, num_vectors=10, vector_length=10):
    """تولید بردارهای تصادفی بدون تکرار اعداد پشت سر هم"""
    random.seed(seed_value)
    vectors = []
    for _ in range(num_vectors):
        while True:
            vector = [random.randint(0, 9) for _ in range(vector_length)]
            if all(vector[i] != vector[i+1] for i in range(vector_length-1)):
                vectors.append(vector)
                break
    return vectors

def print_vectors(vectors, title):
    """نمایش بردارها"""
    print(f"\n{title}:")
    for i, vector in enumerate(vectors, 1):
        print(f"bordar {i}: {' '.join(map(str, vector))}")

def matrix_sum(m1, m2):
    """جمع دو ماتریس"""
    return [[m1[i][j] + m2[i][j] for j in range(10)] for i in range(10)]

def matrix_multiply(m1, m2):
    """ضرب دو ماتریس"""
    result = [[0]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def print_matrix(matrix, title):
    """نمایش زیبای ماتریس"""
    print(f"\n{title}:")
    border = "+" + "-"*23 + "+"
    print(border)
    for row in matrix:
        print("| " + " ".join(f"{x:2}" for x in row) + " |")
    print(border)

def main():
    national_code = input("codemelli ra vared konid: ")
    
    if not (national_code.isdigit() and len(national_code) == 10):
        print("codemelli bayad 10 raghami bashad")
        return
    
    seed = int(hashlib.sha256(national_code.encode()).hexdigest(), 16) % (10**8)
    matrix1 = generate_vectors(seed)
    matrix2 = generate_vectors(seed + 1)

    print("\n" + "="*50)
    print_vectors(matrix1, "bordarhaye matris 1")
    print_vectors(matrix2, "bordarhaye matris 2")

    print("\n" + "="*50)
    print_matrix(matrix1, "matris 1")
    print_matrix(matrix2, "matris 2")

    sum_result = matrix_sum(matrix1, matrix2)
    product_result = matrix_multiply(matrix1, matrix2)

    print("\n" + "="*50)
    print_matrix(sum_result, "jam 2 matris")
    print_matrix(product_result, "zarb 2 matris")

if __name__ == "__main__":
    main()