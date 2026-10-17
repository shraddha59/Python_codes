import math

# Integer
a = 10
b = 3
print("Integer:", a)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Type:", type(a))

# Float
x = 12.5
print("\nFloat:", x)
print("Round:", round(x))
print("Absolute value:", abs(-x))
print("Type:", type(x))

# Complex
c = 4 + 5j
print("\nComplex number:", c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)
print("Type:", type(c))

# String
name = "Python"
print("\nString:", name)
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Type:", type(name))

# List
marks = [80, 85, 90, 95]
print("\nList:", marks)
marks.append(100)
print("After adding element:", marks)
print("Maximum marks:", max(marks))
print("Minimum marks:", min(marks))
print("Total marks:", sum(marks))
print("Type:", type(marks))

# Tuple
numbers = (10, 20, 30, 40)
print("\nTuple:", numbers)
print("Length:", len(numbers))
print("First element:", numbers[0])
print("Count of 20:", numbers.count(20))
print("Type:", type(numbers))

# Dictionary
student = {"name": "Rahul", "age": 20, "marks": 85}
print("\nDictionary:", student)
print("Student name:", student["name"])
student["marks"] = 90
print("Updated dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Type:", type(student))

# Set
s = {10, 20, 30, 40}
print("\nSet:", s)
s.add(50)
print("After adding element:", s)
s.discard(20)
print("After removing element:", s)
print("Type:", type(s))

# Frozenset
fs = frozenset([1, 2, 3, 4])
print("\nFrozenset:", fs)
print("Length:", len(fs))
print("Contains 2:", 2 in fs)
print("Type:", type(fs))

# Boolean
is_pass = True
print("\nBoolean:", is_pass)
print("Logical AND:", True and False)
print("Logical OR:", True or False)
print("Logical NOT:", not is_pass)
print("Type:", type(is_pass))

# NoneType
value = None
print("\nNone value:", value)
print("Is None:", value is None)
print("Type:", type(value))

# Math module functions
print("\nMath Functions")
print("Square root of 25:", math.sqrt(25))
print("Power of 2 and 3:", math.pow(2, 3))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.8:", math.floor(4.8))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print("Absolute value:", math.fabs(-15.5))