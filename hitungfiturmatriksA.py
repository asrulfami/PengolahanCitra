import numpy as np

# Matriks ko-occurrence yang diberikan
co_matrix = np.array([
    [2, 2, 2, 2, 0, 2, 1, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 0, 0, 2],
    [0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2],
    [2, 2, 2, 0, 2, 2, 1, 0, 1, 0],
    [0, 0, 0, 0, 2, 2, 1, 1, 0, 0],
    [0, 0, 0, 2, 2, 1, 2, 0, 0, 0]
])
def calculate_asm(co_matrix):
    return np.sum(np.square(co_matrix))

def calculate_contrast(co_matrix):
    contrast = 0
    for i in range(co_matrix.shape[0]):
        for j in range(co_matrix.shape[1]):
            contrast += (i - j) ** 2 * co_matrix[i, j]
    return contrast

def calculate_correlation(co_matrix):
    px = np.sum(co_matrix, axis=1)
    py = np.sum(co_matrix, axis=0)
    
    ux = np.sum(px * np.arange(co_matrix.shape[0]))
    uy = np.sum(py * np.arange(co_matrix.shape[1]))
    
    sigmax = np.sqrt(np.sum(px * np.square(np.arange(co_matrix.shape[0]) - ux)))
    sigmay = np.sqrt(np.sum(py * np.square(np.arange(co_matrix.shape[1]) - uy)))
    
    correlation = 0
    for i in range(co_matrix.shape[0]):
        for j in range(co_matrix.shape[1]):
            correlation += (i * j * co_matrix[i, j] - ux * uy) / (sigmax * sigmay)
    return correlation

def calculate_dissimilarity(co_matrix):
    dissimilarity = 0
    for i in range(co_matrix.shape[0]):
        for j in range(co_matrix.shape[1]):
            dissimilarity += np.abs(i - j) * co_matrix[i, j]
    return dissimilarity

def calculate_energy(co_matrix):
    return calculate_asm(co_matrix)  # Energy is the same as ASM

# Hitung fitur-fitur
asm_value = calculate_asm(co_matrix)
contrast_value = calculate_contrast(co_matrix)
correlation_value = calculate_correlation(co_matrix)
dissimilarity_value = calculate_dissimilarity(co_matrix)
energy_value = calculate_energy(co_matrix)

# Tampilkan hasil
print("ASM:", asm_value)
print("Contrast:", contrast_value)
print("Correlation:", correlation_value)
print("Dissimilarity:", dissimilarity_value)
print("Energy:", energy_value)
