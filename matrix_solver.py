matrix = [
    [-3, -1, 3, -3],
    [0, -2, -1, 1],
    [3, 2, -3, 0]
]

def equalize_columns(c: int, matrix: list[list[int]]) -> list[list[int]]:
    for r, row in enumerate(matrix):
            if row[c] != 0: 
                divisor = row[c]
                
                for i in range(len(row)):
                    matrix[r][i] /= divisor
    return matrix
    

def subtract_columns(c: int, matrix: list[list[int]]) -> list[list[int]]:
    for r, row in enumerate(matrix):
        if row[c] != 0 and r !=c:
            for i in range(len(row)):
                matrix[r][i] -= matrix[c][i]
    return matrix

def make_zeros_convenient(c: int, matrix: list[list[int]], permutations: int = 0) -> list[list[int]]:
    if matrix[c][c] == 0:
        row1 = matrix[c]
        matrix[c] = matrix[(c+1)%len(matrix)]
        matrix[(c+1)%len(matrix)] = row1
        return make_zeros_convenient(0, matrix, permutations+1)
    elif c >= len(matrix)-2:
        return matrix
    else: return make_zeros_convenient(c+1, matrix, permutations)
    

def solve_matrix(matrix: list[list[int]]) -> list[list[int]]:
    matrix = make_zeros_convenient(0, matrix)

    for c in range(len(matrix[0])-1):
        print(matrix)
        #first, make column equal
        matrix = equalize_columns(c, matrix)
        
            
        print(matrix)
        #then, subtract columns
        
        matrix = subtract_columns(c, matrix)
    print(matrix)
    for c in range(len(matrix[0])-1):
        matrix = equalize_columns(c, matrix)
                    
            
    return matrix

        
m = solve_matrix(matrix)
print(m)
