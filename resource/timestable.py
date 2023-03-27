import sys
n = int(sys.argv[1]) # Note that the items in argv [ ]
file = sys.argv[2] # are strings

# print(n, file)

###Creating the matrixes and making the product
import numpy as np
A=np.random.randint(4, size=(n, n))
B=np.random.randint(4, size=(n, n))
C=np.matmul(A, B)

print("A=",A,"\n")
print("B=",B,"\n")
print("C=",C,"\n")

FileHandle = open(file , 'w')
for i in range(len(C)):
    string="%d\t"*n % tuple(C[i])+"\n"#Print in the file external that we include in second arg in the program
    FileHandle.write(string)
FileHandle.close()
