# Construction of Approximate Real Mutually Unbiased Bases for an infinite class of dimensions d ≢ 0 mod 4
This rproject provides a Python implementation to generate epsilon-Hadamard matrices from any Hadamard matrix whose order is a multiple of 4. It constructs epsilon-Hadamard matrices of order \(4n - t\) for \(t in \{1,2,3\}\), as described in the paper
## Overview
This python code takes Hadamard matrix of order 4n as input, and uses the methods in the paper to construct ε-Hadamard matrices of order 4n-t, where t belongs to {1,2,3}. For each Hadamard matrix, we get 2 ε-Hadamard matrices of a certain order, Y1 and Y2. Then this code checks that the produced matrices are indeed orthogonal. It calculates the ε value for the matrices, and the drift of the elements above and below +1 amd -1. The lesser tha value of ε, the closer is this matrix to the Hadamard matrix, and the better the ARMUBs that can be generated from the methods referenced in the paper. We then save all these outputs to the respective file.
## Steps to run the project

### **1. Requirements**

- Python 3.x  
- numpy

Install dependencies (if not already installed):
pip install numpy

### Running the code
![image](https://github.com/user-attachments/assets/f43c294c-e815-4446-a119-2a594bceab18)  
Here you can choose t value to be 1, 2, or 3
Write the input file and output file path instead of the ones given.
Then run python main.py
The output file will include:
- Order and input Hadamard Matrix
- The 2 constructed ε-Hadamard matrices, Y1 and Y2
- ε values for the 2 ε-Hadamard matrices
- drift of elements of ε-Hadamard matrices above and below 1 and -1.
### Input Hadamard matrix file format
The input file will be in the standard Sloane database format, containing rows of + and -. + represents 1 and - represents -1 for the unnormalized Hadamard matrices. A collection of such files containing Hadamard matrices in almost every dimension where real Hadamard matrices exists can be found in this website: http://neilsloane.com/hadamard/. The sample files for reference are also from this website itself.

### File Structure
The files are labelled as such:
- main.p

##Output example

##Acknowledgement
  
