def bubble_sort(matrix):
    # Mengubah matriks menjadi satu dimensi untuk memudahkan pengurutan
    flat_list = [item for sublist in matrix for item in sublist]
    
    # Bubble Sort
    n = len(flat_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if flat_list[j] > flat_list[j+1]:
                flat_list[j], flat_list[j+1] = flat_list[j+1], flat_list[j]

    return flat_list

def reshape_to_matrix(flat_list, rows, cols):
    matrix = []
    for i in range(0, len(flat_list), cols):
        matrix.append(flat_list[i:i+cols])
    return matrix

def co_occurrence_matrix(matrix, unique_elements):
    element_index = {element: idx for idx, element in enumerate(unique_elements)}
    size = len(unique_elements)
    co_matrix = [[0] * size for _ in range(size)]
    
    # Traverse the matrix to count co-occurrences
    for row in matrix:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                co_matrix[element_index[row[i]]][element_index[row[j]]] += 1
                co_matrix[element_index[row[j]]][element_index[row[i]]] += 1
    
    # Convert counts to 0, 1, or 2
    for i in range(size):
        for j in range(size):
            if co_matrix[i][j] > 1:  # Jika terdapat elemen yang sama lebih dari satu
                co_matrix[i][j] = 2   # Set nilai menjadi 2
            elif co_matrix[i][j] == 1:  # Jika hanya ada satu kemunculan
                co_matrix[i][j] = 1
    
    return co_matrix
    
def total_sum(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total

# Dataset
matrix = [
    [23, 22, 22, 21, 21, 20, 20, 20, 18, 20],
    [22, 21, 21, 21, 20, 20, 19, 19, 19, 21],
    [20, 20, 20, 19, 19, 19, 18, 18, 20, 22],
    [18, 18, 18, 18, 18, 18, 18, 18, 22, 23],
    [17, 17, 17, 18, 18, 18, 18, 18, 22, 24],
    [17, 17, 17, 18, 18, 18, 19, 19, 22, 24],
    [17, 18, 18, 18, 19, 19, 20, 20, 22, 23],
    [18, 18, 18, 19, 19, 20, 20, 21, 21, 22],
    [23, 22, 21, 20, 20, 20, 21, 21, 23, 27],
    [24, 23, 22, 21, 21, 21, 21, 22, 22, 26]
]

# Step 1: Sort the matrix using Bubble Sort
sorted_flat_list = bubble_sort(matrix)

# Step 2: Get unique elements and reshape the sorted list to a matrix
unique_elements = sorted(list(set(sorted_flat_list)))
sorted_matrix = reshape_to_matrix(sorted_flat_list, 10, 10)

# Step 3: Create the co-occurrence matrix
co_matrix = co_occurrence_matrix(matrix, unique_elements)

# Print results
print("Sorted Matrix:")
for row in sorted_matrix:
    print(row)
print('________________________________________________')    
print("Unique Elements:", unique_elements)
print('________________________________________________')
print("Co-occurrence Matrix with Elements:")
print("   ", ','.join(map(str, unique_elements)))

for idx, row in enumerate(co_matrix):
    print(f"{str(unique_elements[idx]):<15}", ','.join(map(str, row)))

# Total sum of the co-occurrence matrix
total_sum_value = total_sum(co_matrix)
print("Total jumlah seluruh data dalam matriks:", total_sum_value)

# Menampilkan matriks co-occurrence sebagai pecahan dari total jumlah data
print("\nCo-occurrence Matrix sebagai pecahan dari total jumlah data:")
for i in range(len(co_matrix)):
    row_output = []
    for j in range(len(co_matrix[i])):
        if co_matrix[i][j] == 0:
            row_output.append('0')
        else:
            row_output.append(f'{co_matrix[i][j]}/{total_sum_value}')
    print(', '.join(row_output))
