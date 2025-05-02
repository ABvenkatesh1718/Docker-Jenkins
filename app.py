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
import sys

import argparse

parser = argparse.ArgumentParser(description="Accept name and age.")
parser.add_argument('--name', type=str, required=True, help="Your name")
parser.add_argument('--age', type=int, required=True, help="Your age")

args = parser.parse_args()

print(f"Welcome {args.name}, your age is {args.age}!")
