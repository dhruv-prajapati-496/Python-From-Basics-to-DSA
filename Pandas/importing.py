import pandas as pd

# This file shows how to import CSV (Comma-separated Values) and JSON (Java Script Object Notation) Files.
df = pd.read_csv("C:/Coding/Python Learning Journey/Pandas/read_csv.csv")
print(df)

df1 = pd.read_json("C:/Coding/Python Learning Journey/Pandas/read_json.json")
print(df1)
# Now you can see that the complete data is not printed, to print the complete data, we've to write this command -> print(df.to_string())

