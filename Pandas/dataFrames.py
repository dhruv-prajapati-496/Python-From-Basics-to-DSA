import pandas as pd

# Data Frames : A Tabular data structure with ROWS and COLUMNS. (2 dimensional like a ms excel spreadsheet)

d1 = {"Name": ["Aditya","Om","Rishav"],
      "Age": [23,34,38]}
df = pd.DataFrame(d1)
print(df)

# We can also set index. By default the index starts from 0. 
df1 = pd.DataFrame(d1,index=["Employee 1","Employee 2", "Employee 3"])
print(df1)

# We can also access the data using index.
print(df.loc[2])
print(df1.loc["Employee 2"])
print(df1.iloc[2])

# Add a New Column
df1["Job"] = ["Cook", "N/A","General Manager"]
print(df1)

# Add a new row
# To add a new row, we have to create a new dataframe and then concatenate it.
new_row = pd.DataFrame([{"Name": "Tony", "Age": 45, "Job": "Scientist"}],
                       index=["Employee 4"]) # creating a new data frame, without index it'll assigned to 0.
df1 = pd.concat([df1,new_row])
print(df1)