import numpy as np

# Creating a 1D array
a = np.array([10, 20, 30, 40, 50])
print("One Dimensional Array:")
print(a)

# Indexing
print("\nFirst element:", a[0])
print("Third element:", a[2])

# Slicing
print("First three elements:", a[0:3])
print("Last two elements:", a[3:5])

# Creating an array using arange()
b = np.arange(1, 11)
print("\nArray using arange:")
print(b)

# Creating an array using linspace()
c = np.linspace(1, 10, 5)
print("\nArray using linspace:")
print(c)

# Mathematical operations
print("\nSum of array:", np.sum(a))
print("Mean of array:", np.mean(a))
print("Addition:", a + 5)
print("Multiplication:", a * 2)

# Creating a 2D array
d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTwo Dimensional Array:")
print(d)

# Indexing in 2D array
print("\nElement at row 1, column 2:", d[0, 1])
print("Element at row 2, column 3:", d[1, 2])

# Slicing in 2D array
print("\nFirst row:")
print(d[0, :])

print("Second column:")
print(d[:, 1])

# Reshaping an array
e = np.arange(1, 13)
print("\nOriginal Array:")
print(e)

f = np.reshape(e, (3, 4))
print("Reshaped Array (3x4):")
print(f)

# Mathematical functions on 2D array
print("\nSum of all elements:", np.sum(d))
print("Mean of all elements:", np.mean(d))
print("Sum of each row:", np.sum(d, axis=1))
print("Sum of each column:", np.sum(d, axis=0))