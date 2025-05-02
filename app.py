import pandas as pd

# Dummy dataset
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["NY", "LA", "Chicago", "Houston"],
    "marks": [85, 78, 92, 65]
}

df = pd.DataFrame(data)

# Filter names with marks > 80
top_students = df[df["marks"] > 80]

print("Students with marks > 80:")
print(top_students["name"].to_list())
