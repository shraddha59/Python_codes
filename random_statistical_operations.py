import numpy as np

# Generate random numbers between 0 and 1
a = np.random.rand(5)
print("Random numbers:")
print(a)

# Generate normally distributed random numbers
b = np.random.randn(5)
print("\nRandom normal numbers:")
print(b)

# Generate random integers
c = np.random.randint(1, 100, 5)
print("\nRandom integers:")
print(c)

# Generate numbers using normal distribution
d = np.random.normal(50, 10, 5)
print("\nNormal distribution:")
print(d)

# Calculate statistics
print("\nStatistical Operations")
print("Sum:", np.sum(c))
print("Mean:", np.mean(c))
print("Maximum:", np.max(c))
print("Minimum:", np.min(c))
print("Standard deviation:", np.std(c))
print("Variance:", np.var(c))