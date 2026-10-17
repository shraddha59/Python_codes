import numpy as np

# Creating two arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("First Array:")
print(a)

print("Second Array:")
print(b)

# Vectorized addition
print("\nAddition of two arrays:")
print(np.add(a, b))

# Vectorized subtraction
print("\nSubtraction of two arrays:")
print(a - b)

# Vectorized multiplication
print("\nMultiplication of two arrays:")
print(a * b)

# Square root using universal function
print("\nSquare root of array:")
print(np.sqrt(a))

# Exponential function
print("\nExponential values:")
print(np.exp(b))

# Broadcasting with a single number
print("\nAdding 5 to each element:")
print(a + 5)

# Broadcasting with two arrays
x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([10, 20, 30])

print("\nTwo Dimensional Array:")
print(x)

print("One Dimensional Array:")
print(y)

print("\nResult after broadcasting:")
print(x + y)

# Broadcasting with multiplication
print("\nMultiplication using broadcasting:")
print(x * 2)

# Using np.add with broadcasting
print("\nAddition using np.add:")
print(np.add(x, y))