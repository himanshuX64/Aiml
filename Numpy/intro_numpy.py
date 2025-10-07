import numpy as np
from numpy.linalg import inv, det, eig, svd, norm
# Create a 1-dimensional NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)


# Access elements in the 1D array
print("First element:", array_1d[0])
print("Last element:", array_1d[-1])


# Modify an element in the 1D array
array_1d[2] = 10
print("Modified 1D Array:", array_1d)


# Perform basic operations on the 1D array
print("Sum of elements:", np.sum(array_1d))
print("Mean of elements:", np.mean(array_1d))  
print("Standard deviation of elements:", np.std(array_1d))
print("Maximum element:", np.max(array_1d)) 
print("Minimum element:", np.min(array_1d))
print("Sorted Array:", np.sort(array_1d))   
print("Array shape:", array_1d.shape)
print("Array data type:", array_1d.dtype)


# Create a 3x3 identity matrix
print(np.eye(3))


# Create an array with a step of 2
print(np.arange(1, 10, 2))  


# 5 evenly spaced numbers between 1 and 10
print("Array with linspace:", np.linspace(1, 10, 5)) 

#Create a Empaty array
empaty_arr=np.empty((2,3))
print("Empty Array:", empaty_arr)


#Create an arrray` of evenly spaced numbers
even_spaced_arr = np.arange(0, 45,2)
print(even_spaced_arr)


# Array Properties
#dimention
print(array_1d.shape)
# Number of dimensions
print("Number of Dimention",array_1d.ndim)
# Data type of the array
print("Data types of Araay",array_1d.dtype)
# Number of elements in the array
print("Number of elements in the array:", array_1d.size)


# Indexing and Slicing
# Accessing a range of elements
arr=np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("Slicing elements from index 1 to 3:", arr[1:4])


# Slicing with a step 2d Array
arr_2d=np.array([[101, 102, 103], [201, 202, 203], [301, 302, 303]])
print("2D Array:\n",arr_2d[0,2])
print("2d Array :\n",arr_2d[:2,1:])


#Boolean  Indexing(Filtering data)
print("Filtering array :",arr_2d[arr_2d>106])


# Vectorized Operation
a=np.array([1,2,3])
b=np.array([4,5,6])
print("Adding,  multiply,  SubsTraction :",a+b,a*b,a-b)

#Dot Product
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)

# Broadcasting
c = np.array([[10, 20, 30],[40, 50, 60]])
d=np.array([1, 2, 3])
print("Broadcasting Addition:", c + d)


# Linear Algebra Operations(core Ml mathematics)
# first of all linalg module is imported --> from numpy.linalg import inv, det, eig, svd, norm
C= np.array([[1, 2], [3, 4]])
print(inv(C))  # Inverse of a matrix
print(det(C)) # Determinant of a matrix
print(eig(C)) # Eigenvalues and eigenvectors of a matrix
print(svd(C)) # Singular Value Decomposition of a matrix
print("Vector norm:", norm(C))  # Vector norm


#statistics
data = np.random.randn(100)  # Generate random data
print("Mean:", np.mean(data))           # Mean
print("Median:", np.median(data))       # Median
print("Standard Deviation:", np.std(data))  # Standard Deviation
print("Variance:", np.var(data))        # Variance
print("25th Percentile:", np.percentile(data, 25))  # 25th Percentile


# Reshaping and Resizing
arr_reshaped = np.arange(24).reshape(8,3)
print("Reshaped Array:\n", arr_reshaped)
print("Converted to 1D Array:", arr_reshaped.flatten())


