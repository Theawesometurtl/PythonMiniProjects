from math import sin, radians, cos

t1 = 45
t2 = 90 - t1
t3 = 20
t4 = radians(t2 - t3)
t2 = radians(t2)
L = 100

matrix = [
        [sin(t2),sin(t2),0,0,0,0,0,0,0,0,L],
        [cos(t2),-cos(t2),0,0,0,0,0,0,0,0,0],
        [-sin(t2),0,sin(t4),sin(t2),cos(t4),0,0,0,0,0,0],
        [-cos(t2),0,cos(t4),cos(t2),sin(t4),0,0,0,0,0,0],
        [0,0,-sin(t4),0,0,0,0,1,0,0,0],
        [0,0,-cos(t4),0,0,1,0,0,0,0,0],
        [0,0,0,-sin(t2),0,0,-1,0,0,sin(t2),0],
        [0,0,0,-cos(t2),0,-1,0,0,0,cos(t2),0],
        [0,0,0,0,-sin(t4),0,0,0,1,0,0],
        [0,0,0,0,-cos(t4),0,1,0,0,0,0],
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
    # matrix = make_zeros_convenient(0, matrix)
    r=0
    previously_swapped_r = len(matrix)+1
    while True:
        if matrix[r][r] == 0:
            for i, row in enumerate(matrix):
                if row[r] != 0 and previously_swapped_r != i:
                    row_save = matrix[r]
                    matrix[r] = matrix[i]
                    matrix[i] = row_save
                    break
            previously_swapped_r = r
            r=0
        elif r+1 >= len(matrix):
            break
        else: r+=1



    for c in range(len(matrix[0])-1):
        # print(matrix)
        #first, make column equal
        matrix = equalize_columns(c, matrix)
        
            
        # print(matrix)
        #then, subtract columns
        
        matrix = subtract_columns(c, matrix)
    # print(matrix)
    for c in range(len(matrix[0])-1):
        matrix = equalize_columns(c, matrix)
                    
            
    return matrix

        
m = solve_matrix(matrix)
for row in matrix:
    print(row)
