import numpy as np
import math
# This code works for any Hadamard matrix which is a multiple of 4, and creates epsilon-Hadamard matrices of order 4n-t, t ={1,2,3}
# Change t from here to be 1,2,3 as you like
t = 3
# Choose input and output file from here
input_file = "had.80.pal.txt"
output_file = "output_80-1.txt"
ortho_threshold = 0.000000000000001  #threshold for dot product of rows in an orthogonal matrix, not 0 exactly due to floating point round off error
# Create the epsilon-Hadamard matrices Y1, Y2
"""
Y1, Y2 = epsilon-Hadamard matrices of order 4n-t
U, V, W, D = sub-blocks of Hadamard matrices when written in block form
I = identity matrix or order t
inv1, inv2 = Inverse of (I+U) and (I-U) respectively
"""
def eHadamard(H, n, t):
    # separating the blocks of the Hadamard matrix
    U = H[0:t, 0:t]
    V = H[0:t, t:4*n]
    W = H[t:4*n, 0:t]
    D = H[t:4*n, t:4*n]
    I = np.eye(t) 
    try:
        inv1 = np.linalg.inv(I + U)
        Y1 = (D - (W @ inv1 @ V))
    except np.linalg.LinAlgError:
        print("Error: (I + U) is singular and cannot be inverted. Try a different Hadamard matrix")
        exit(0)
    try:
        inv2 = np.linalg.inv(I-U)
        Y2 = (D + (W @ inv2 @V))
    except np.linalg.LinAlgError:
        print("Error: (I - U) is singular and cannot be inverted. Try a different Hadamard matrix")
        exit(0)
    return Y1, Y2

# Orthogonality check of 4n-t x 4n-t matrix Y
"""
flag = flag variable for orthogonality of matrix Y
ortho_threshold = threshold below which the dot product of rows should be for the matrix to be orthogonal
it is not 0 here, due to floating point rounding errors.
"""
def ortho(Y, n, t):
    flag = 0
    for i in range(4*n-t):
        for j in range(4*n-t):
            if i != j:
                if (np.dot(Y[i], Y[j]) > ortho_threshold or np.dot(Y[i], Y[j]) < -1*ortho_threshold):
                    flag = 1
                    break
    if flag == 0:
        print("Yes, orthogonal matrix")
    else:
        print("No, not orthogonal matrix")

# calculate epsilon of epsilon-Hadamard matrix Y
"""
e = epsilon value for each element in matrix
max = maximum value of |e|
drift_above_1, drift_below_1, drift_above_n1, drift_below_n1 each stores maximum drift above and below 1 and -1
"""
def epsilon(Y, n, t):
    max = 0
    drift_above_1, drift_below_1, drift_above_n1, drift_below_n1 = (0, 0, 0, 0)
    for i in range(4*n-t):
        for j in range(4*n-t):
            element = Y[i][j] * math.sqrt(4*n-t)
            e = np.abs(element)-1
            if abs(e) > max:
                max = abs(e)
            if element >1:
                if (element - 1) > drift_above_1:
                    drift_above_1 = element -1
            if element <1 and element >0:
                if (1-element) > drift_below_1:
                    drift_below_1 = 1 - element
            if element > -1 and element < 0:
                if (element +1) > drift_above_n1:
                    drift_above_n1 = element+1
            if element <-1:
                if (-1 - element) > drift_below_n1:
                    drift_below_n1 = -1 - element
    return max, drift_above_1, drift_below_1, drift_above_n1, drift_below_n1

# Read hadamard matrix from file 
"""
Read Hadamard matrix from filepath
file contains + and - characters, + representing 1 and - representing -1 of an unnormalized Hadamard matrix
database of Hadamard matrices with such files: http://neilsloane.com/hadamard/
lines = list of strings from the file
line = each string in lines
char = each character in line
d = size of Hadamard matrix = 4*n
"""
def read_hadamard(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    matrix = []
    for line in lines:
        row = []
        for char in line.strip():
            if char == '+':
                row.append(1)
            elif char == '-':
                row.append(-1)
        matrix.append(row)
    H = np.array(matrix)
    d = H.shape[0]
    H = (1/np.sqrt(d))*H
    return H, (d//4)
# output: output to the file
output = "" 
H, n = read_hadamard(input_file)
print("order is ", 4*n)
print("Hadamard matrix is: ", H)
output += f"order is:{4*n}\n"
output += f"Hadamard matrix is:\n{H}\n"
Y1, Y2= eHadamard(H, n, t)
print("The epsilon-Hadamard matrices we get are: ")
print("Y1: ", Y1)
print("Y2: ", Y2)
output += f"The epsilon-Hadamard matrices we get of order {4*n - t} are:\n"
output += f"Y1 :\n{Y1}\n"
output += f"Y2 :\n{Y2}\n"
# Check for orthogonality of the epsilon-Hadamard matrices
print("Y1 check for orthogonality:")
ortho(Y1, n, t)
print("Y2 check for orthogonality:")
ortho(Y2, n, t)
print("Epsilon values for the Hadamard matric used and the epsilon-Hadamard matrices created")
output += "Epsilon values for the epsilon-Hadamard matrices created\n"
epsi, drift_above_1, drift_below_1, drift_above_n1, drift_below_n1 = epsilon(H, n, 0)
print("e_Hadamard: ", epsi)
epsi, drift_above_1, drift_below_1, drift_above_n1, drift_below_n1 = epsilon(Y1, n, t)
output += f"e_Y1: {epsi}, drift_above_1: {drift_above_1}, drift_below_1: {drift_below_1}, drift_above_n1: {drift_above_n1}, drift_below_n1: {drift_below_n1}\n"
print("e_Y1: ", epsi)
epsi, drift_above_1, drift_below_1, drift_above_n1, drift_below_n1 = epsilon(Y2, n, t)
output += f"e_Y2: {epsi}, drift_above_1: {drift_above_1}, drift_below_1: {drift_below_1}, drift_above_n1: {drift_above_n1}, drift_below_n1: {drift_below_n1}\n"
print("e_Y2: ", epsi)


with open(output_file, "w") as f:
    f.write(output)