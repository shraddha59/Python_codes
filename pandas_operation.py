import pandas as pd

# Creating a Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Student Marks:")
print(marks)

# Creating a DataFrame
data = {
    "Name": ["Shraddha", "Shruti", "Durva", "Shravani", "Shreya"],
    "Age": [18, 19, 18, 20, 19],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

# Display first five rows
print("\nFirst Rows:")
print(df.head())

# Display last two rows
print("\nLast Two Rows:")
print(df.tail(2))

# Display basic statistics
print("\nStatistical Information:")
print(df.describe())

# Basic operations
print("\nStudent Names:")
print(df["Name"])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

# Adding a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)

# Exporting data to CSV
df.to_csv("students.csv", index=False)
print("\nData saved to students.csv")

# Importing data from CSV
new_df = pd.read_csv("students.csv")

print("\nData Imported from CSV:")
print(new_df)